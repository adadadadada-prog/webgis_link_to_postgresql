from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class VectorLayer(Base):
    __tablename__ = "vector_layers"
    id: Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    description: Mapped[str | None] = mapped_column(Text,nullable=True)

    # 这里的类型可以更换为更准确的类别
    geometry_type: Mapped[str] = mapped_column(String(100),nullable=False)
    srid: Mapped[int] = mapped_column(Integer,default=4326,nullable=False)

    table_name:Mapped[str] = mapped_column(String(100),unique=True,nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),

    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate= func.now(),
    )