Contributing
============

Making a development environment
--------------------------------

* Checkout the source code::

  $ git clone git@github.com:Shoobx/pyocf.git

* Create a development environment::

  $ make devenv

* Check out the OCF schema that you are developing on into the pyocf folder.
  To get the latest version, you can simply do::

  $ make fetch

* To generate the pyocf code from the OCF schema run::

  $ make generate

* And to run the tests::

  $ make tests

* Before you make a pull request, make sure the code passes the formatting tests::

  $ make check

* You can also verify the coverage with::

  $ make coverage

If you just run ``make`` with no further parameters, make will fetch the latest
OCF schema, generate the pyocf code from it, and update the API documentation.


Making pull requests
--------------------

Your pull request should fulfill the following requirements.

* Pass all the checks, including but not limited to all tests, formatting and
  converage checks.

* Include a description of the problem being solved, and in complex cases, an
  explanation of how the problem was solved.

* Include an update of the CHANGES.rst to summarize the change.

* Your name should be in the Contributors list in the README.rst.


Releasing
---------

We use ``zest.releaser`` to do the releases. To use ``zest.releaser`` you need
to have a ``.pypirc`` set up, and of course privileges to release ``pyocf``.

Before making a release, make sure that the CHANGES.txt is updated, and that
all changes are pushed to the VCS. Then run ``make check test`` to check that
the style and formatting is correct, and that all tests pass.

Then use ``fullrelease`` to make a release and upload it to PyPI.
