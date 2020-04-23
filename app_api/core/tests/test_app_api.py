from django.urls import reverse

from mixer.backend.django import mixer
import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def some_app():
    return mixer.blend('app', pk=100500)


@pytest.mark.django_db
def test_app_list(some_app, api_client):
    got = api_client.get(reverse('app-list'))

    assert got.status_code == 200
    assert len(got.json()) == 1


@pytest.mark.django_db
def test_app_retrieve(some_app, api_client):
    got = api_client.get(reverse('app-detail', kwargs={'pk': 100500}))

    assert got.status_code == 200
    assert got.json()['id'] == 100500


@pytest.mark.django_db
def test_app_api_key_is_generated_on_post(some_app, api_client):
    data = {
        'name': 'test_name'
    }
    got = api_client.post(reverse('app-list'), data=data)

    assert got.status_code == 201
    assert got.json()['api_key'] is not None


@pytest.mark.django_db
def test_app_accessible_by_api_key(some_app, api_client):
    kwargs = {'api_key': some_app.api_key}
    got = api_client.get(reverse('app-api-key', kwargs=kwargs))

    assert got.status_code == 200
    assert got.json()['name'] == some_app.name
    assert got.json()['id'] == some_app.pk
    assert got.json()['api_key'] == some_app.api_key


@pytest.mark.django_db
def test_app_api_key_can_be_regenerated_and_not_updated(some_app, api_client):
    data = {
        'api_key': 'someuselessapikeythatwontwork'
    }

    kw = {'pk': 100500}
    got = api_client.put(reverse('update-key', kwargs=kw), data=data)

    assert got.status_code == 200
    assert got.json()['api_key'] != some_app.api_key
    assert got.json()['api_key'] != data['api_key']


@pytest.mark.django_db
def test_app_update_works_on_name(some_app, api_client):
    data = {
        'name': 'new_name',
    }
    kw = {'pk': 100500}
    got = api_client.put(reverse('app-detail', kwargs=kw), data=data)

    assert got.status_code == 200
    assert got.json()['id'] == 100500
    assert got.json()['name'] != some_app.name
    assert got.json()['name'] == data['name']


@pytest.mark.django_db
def test_app_update_doesnt_work_on_api_key(some_app, api_client):
    data = {
        'name': 'new_name',
        'api_key': 'new_key'
    }
    kw = {'pk': 100500}
    got = api_client.put(reverse('app-detail', kwargs=kw), data=data)
    print(got.json())

    assert got.status_code == 200
    assert got.json()['id'] == 100500
    assert got.json()['api_key'] == some_app.api_key
    assert got.json()['api_key'] != data['api_key']
