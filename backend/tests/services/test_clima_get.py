from Products.CMFPlone.Portal import PloneSite

import pytest


@pytest.mark.portal(
    content=[
        {"type": "Document", "id": "colaboradores", "title": "Pasta de Colaboradores"}
    ],
)
class TestServiceClimaGet:
    portal: PloneSite
    endpoint: str = "/@clima"

    @pytest.fixture(autouse=True)
    def _setup(self, functional_portal, patch_openmeteo):
        self.portal = functional_portal

    def test_get_status_code(self, manager_request):
        response = manager_request.get(self.endpoint)
        assert response.status_code == 200

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["@id", True],
            ["events", True],
            ["temperature", True],
            ["weather", True],
        ],
    )
    def test_get_keys(self, manager_request, key: str, expected: bool):
        response = manager_request.get(self.endpoint)
        data = response.json()
        assert (key in data) is expected

    def test_fails_anon_user(self, anon_request):
        """Usuário anônimo não deve ter acesso ao serviço de clima."""
        response = anon_request.get(self.endpoint)
        assert response.status_code == 401

    def test_only_accessible_on_root(self, manager_request):
        """Usuário anônimo não deve ter acesso ao serviço de clima."""
        url = f"/colaboradores{self.endpoint}"
        response = manager_request.get(url)
        assert response.status_code == 404

    @pytest.mark.parametrize(
        "localidade,status_code",
        [
            ["brasilia", 200],
            ["mooca", 200],
            ["curitiba", 200],
            ["localidade_inexistente", 400],
        ],
    )
    def test_get_localidade(self, manager_request, localidade: str, status_code: int):
        """Testa se a localidade retornada é a esperada."""
        url = f"{self.endpoint}?localidade={localidade}"
        response = manager_request.get(url)
        data = response.json()
        assert response.status_code == status_code
        if status_code == 200:
            assert data["localidade"] == localidade
