from pydantic import BaseModel

def update_item(item: BaseModel) -> None:
    item.save()