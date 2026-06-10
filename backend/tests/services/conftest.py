from pathlib import Path

import json
import pytest


LOCAL_PATH = Path(__file__).parent


@pytest.fixture(scope="session")
def openmeteo_response():
    raw_data = (LOCAL_PATH / "openmeteo.json").read_text()
    return json.loads(raw_data)


@pytest.fixture
def patch_openmeteo(monkeypatch, openmeteo_response):
    from v2tec.intranet.utils import openmeteo

    def mockreturn(params):
        return openmeteo_response

    monkeypatch.setattr(openmeteo, "_obtem_dados_open_meteo", mockreturn)
