from uuid import UUID as UUIDType
from typing import Any, List

from sqlalchemy import (
    INT,
    ForeignKey,
    PrimaryKeyConstraint,
    Table,
    MetaData,
    ForeignKey,
    Column,
    String,
    inspect,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID, TEXT, JSONB


convention = {
    "all_column_names": lambda constraint, _: "_".join(
        [column.name for column in constraint.columns.values()]
    ),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s',
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=convention)  # type: ignore
    type_annotation_map = {dict[str, Any]: JSONB}

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


contest_problem_table = Table(
    'contest_problem_association',
    Base.metadata,
    Column('contest_id', ForeignKey('contest.id')),
    Column('problem_id', ForeignKey('problem.id')),
)

contest_participant_table = Table(
    'contest_participant_association',
    Base.metadata,
    Column('contest_id', ForeignKey('contest.id')),
    Column('participant_id', ForeignKey('user.id')),
)


class User(Base):
    __tablename__ = 'user'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    login: Mapped[str] = mapped_column(String(124), nullable=False)
    password: Mapped[str] = mapped_column(String(124), nullable=False)
    full_name: Mapped[TEXT] = mapped_column(TEXT, nullable=False)


class Problem(Base):
    __tablename__ = 'problem'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    title: Mapped[str] = mapped_column(String(124), nullable=False)
    memory_limitation: Mapped[int] = mapped_column(INT, nullable=False)
    time_limitation: Mapped[int] = mapped_column(INT, nullable=False)
    text: Mapped[str] = mapped_column(TEXT, nullable=False)
    input_file: Mapped[str] = mapped_column(String(124), nullable=False)
    output_file: Mapped[str] = mapped_column(String(124), nullable=False)


class Contest(Base):
    __tablename__ = 'contest'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    problems: Mapped[List[Problem]] = relationship(
        secondary=contest_problem_table
    )
    participants: Mapped[List[Problem]] = relationship(
        secondary=contest_participant_table
    )


class Solution(Base):
    __tablename__ = 'solution'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    code: Mapped[str] = mapped_column(TEXT, nullable=False)
    problem: Mapped[UUIDType] = mapped_column(ForeignKey('problem.id'))
    user: Mapped[UUIDType] = mapped_column(ForeignKey('user.id'))
    verdicts: Mapped[List['TestVerdict']] = relationship(
        back_populates="test_verdicts"
    )


class Test(Base):
    __tablename__ = 'test'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    problem: Mapped[UUIDType] = mapped_column(ForeignKey('problem.id'))
    input: Mapped[str] = mapped_column(TEXT, nullable=False)
    output: Mapped[str] = mapped_column(TEXT, nullable=False)


class TestVerdict(Base):
    __tablename__ = 'test_verdict'
    id: Mapped[UUIDType] = mapped_column(UUID, primary_key=True)
    verdict: Mapped[str] = mapped_column(String(2), nullable = False)
    compilation_output: Mapped[str] = mapped_column(TEXT, nullable = False)
    runtime_output: Mapped[str] = mapped_column(TEXT, nullable = False)
    used_ram: Mapped[int] = mapped_column(INT, nullable=False)    # Bytes
    used_time: Mapped[int] = mapped_column(INT, nullable=False)   # Miliseconds
    test = mapped_column(ForeignKey('test.id'))
    solution = mapped_column(ForeignKey('solution.id'))
