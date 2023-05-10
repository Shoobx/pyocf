"""A pydantic model for simple types with no attributes"""

# Copyright © 2023 FMR LLC

from pydantic import BaseModel


class SimpleBaseModel(BaseModel):
    """A pydantic model for simple types with no attributes

    This model allows you to pass the value into object initialization
    without a name, instead of passing it in as ``__root__``.
    """

    def __init__(self, __root__):
        # In the basemodel, you have to pass in the value as __root__,
        # here you can pass it as a value, as it's the only parameter.
        super().__init__(__root__=__root__)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return super().__eq__(other)

        return self.__root__ == other

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return super().__ge__(other)

        return self.__root__ >= other

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return super().__gt__(other)

        return self.__root__ > other

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return super().__le__(other)

        return self.__root__ <= other

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return super().__lt__(other)

        return self.__root__ < other

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return super().__ne__(other)

        return self.__root__ != other
