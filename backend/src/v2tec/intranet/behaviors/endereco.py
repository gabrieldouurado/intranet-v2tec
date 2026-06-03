from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from v2tec.intranet import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IEndereco(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "dados_endereco",
        _("Endereço"),
        fields=[
            "endereco",
            "complemento",
            "cidade",
            "estado",
            "cep",
        ],
    )

    endereco = schema.TextLine(
        title=_("Endereço"),
        description=_("Informe o endereço da área"),
        required=False,
    )

    complemento = schema.TextLine(
        title=_("Complemento"),
        description=_("Informe o complemento do endereço do endereço"),
        required=False,
    )

    cidade = schema.TextLine(
        title=_("Cidade"),
        description=_("Informe a cidade da área"),
        required=False,
    )

    estado = schema.Choice(
        title=_("Estado"),
        description=_("Informe o estado da área"),
        vocabulary="v2tec.intranet.vocabulary.estados",
        required=False,
    )

    cep = schema.TextLine(
        title=_("CEP"),
        description=_("Informe o CEP da área"),
        required=True,
    )
