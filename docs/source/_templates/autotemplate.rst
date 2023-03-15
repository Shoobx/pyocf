{{ fullname | escape | underline}}

.. automodule:: {{ fullname }}
   :members:
   :undoc-members:

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :recursive:
   :template: autotemplate.rst

{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}
