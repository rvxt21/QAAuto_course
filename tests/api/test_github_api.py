import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')

    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('golang_projector_homeworks')

    assert r['total_count'] == 1
    assert 'golang_projector_homeworks' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('golang_projector_homeworks_non exists')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_emoji(github_api):
    r = github_api.search_emoji()

    assert r.status_code == 200

@pytest.mark.api
def test_list_of_commits(github_api):
    r = github_api.search_list_of_commits('rvxt21',
                                          'golang_projector_homeworks')
    assert r.status_code == 200

@pytest.mark.api
def test_list_of_commits_with_wrong_reponame(github_api):
    r = github_api.search_list_of_commits('rvxt21', 'projector_homeworks')

    assert r.status_code == 404
    assert r.reason == 'Not Found'

