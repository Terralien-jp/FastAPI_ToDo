from typing import Optional

from pydantic import BaseModel, field


class Task(BaseModel):
    id: int
    title: Optionai[str] = Field(None, example="クリーニングを鶏肉")
    done: bool = FIeld(False, description="完了フラグ")