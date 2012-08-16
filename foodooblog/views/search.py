"""The search bar form related classes and the views that get there aswell."""

from colander import Schema
from colander import SchemaNode
from colander import String
from deform import Form
from deform import widget

def gen_search_bar():
    class SearchSchema(Schema):
        terms = SchemaNode(String(), widget=widget.TextInputWidget(size=40), dscription="Search")

    myschema = SearchSchema()
    form = Form(myschema)

    return form.render()
