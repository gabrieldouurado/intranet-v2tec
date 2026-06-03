from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from zope.component.hooks import setSite

import pytest
import transaction


@pytest.fixture
def portal_factory(functional_portal):
    def func(behavior: str):
        setRoles(functional_portal, TEST_USER_ID, ["Manager"])
        fti = DexterityFTI("DummyType")
        fti.behaviors = (behavior,)
        functional_portal.portal_types._setObject("DummyType", fti)
        setSite(functional_portal)
        transaction.commit()
        return functional_portal

    return func


@pytest.fixture
def dummy_type_schema(manager_request):
    def func():
        url = "/@types/DummyType"
        response = manager_request.get(url)
        data = response.json()
        return data

    return func


@pytest.fixture
def create_dummy_content(manager_request):
    def func(payload: dict):
        payload["@type"] = "DummyType"
        response = manager_request.post("/", json=payload)
        return response

    return func
