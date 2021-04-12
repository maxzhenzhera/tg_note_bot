"""
Implements db models.

.. class:: Users(Base)
.. class:: Rubrics(Base)
.. class:: Links(Base)
"""

from aiogram.utils import markdown as md

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    func,
    Integer,
    String,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship
)
from sqlalchemy.exc import MissingGreenlet


Base = declarative_base()


class User(Base):
    """ Implements telegram user model """

    __tablename__ = 'users'

    # basically, it supposed to be a telegram id
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    rubrics = relationship('Rubric', back_populates='user', order_by='Rubric.name')
    links = relationship('Link', back_populates='user', order_by='Link.url')

    def __repr__(self):
        return f'User(id={self.id!r}, created_at={self.created_at!r})'


class Rubric(Base):
    """ Implements link rubrics model """

    __tablename__ = 'rubrics'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='rubrics')
    links = relationship('Link', back_populates='rubric', order_by='Link.url')

    def __repr__(self):
        return (
            f'Rubric(id={self.id!r}, name={self.name!r}, description={self.description!r}, '
            f'created_at={self.created_at!r}, user_id={self.user_id!r})'
        )

    @property
    def short_tg_repr(self) -> str:
        """ Return bold name of the rubric """
        return md.hbold(self.name)

    @property
    def full_tg_repr(self) -> str:
        """ Return short repr with description in square brackets if exists """
        return md.text(self.short_tg_repr, f'[{self.description}]') if self.description else self.short_tg_repr

    def repr_with_link(self, link_shift: str, *, rubric_shift: str = '') -> str:
        """
        Return formatted list of the rubric links.

        :return: formatted list of the rubric links
        :rtype: str

        :raises MissingGreenlet: raised if rubric was not loaded with links
        """
        rubric_links = self.links
        if rubric_links:
            text = md.text(
                f'{rubric_shift} {self.short_tg_repr}',
                *[
                    f'{rubric_shift} {link_shift} {link.tg_repr}'
                    for link in self.links
                ],
                sep='\n'
            )
        else:
            text = md.text(f'{rubric_shift} {self.short_tg_repr} [empty]')

        return text


class Link(Base):
    """ Implements link model """

    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.current_timestamp())

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    rubric_id = Column(Integer, ForeignKey('rubrics.id', ondelete='SET NULL'))

    user = relationship('User', back_populates='links')
    rubric = relationship('Rubric', back_populates='links')

    def __repr__(self):
        return (
            f'Link(id={self.id!r}, url={self.url!r}, description={self.description!r}, '
            f'created_at={self.created_at!r}, user_id={self.user_id!r}, rubric_id={self.rubric_id})'
        )

    @property
    def short_url(self) -> str:
        return self.url.removeprefix('http://').removeprefix('https://').removeprefix('www.')

    @property
    def tg_repr(self) -> str:
        """ Hide link in the description if exists else hide link displaying in url """
        return f'{md.hlink(self.description, self.url)}\n[{self.short_url}]' if self.description else self.short_url

