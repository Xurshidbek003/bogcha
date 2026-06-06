from sqlalchemy.orm import Session
import models, schemas


def get_kindergartens(db: Session, region: str = None, type: str = None):
    query = db.query(models.Kindergarten)
    if region:
        query = query.filter(models.Kindergarten.region.ilike(f"%{region}%"))
    if type:
        query = query.filter(models.Kindergarten.type == type)
    return query.all()


def get_kindergarten(db: Session, kg_id: int):
    return db.query(models.Kindergarten).filter(models.Kindergarten.id == kg_id).first()


def create_kindergarten(db: Session, item: schemas.KindergartenCreate):
    db_item = models.Kindergarten(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_kindergarten(db: Session, kg_id: int, item: schemas.KindergartenUpdate):
    db_item = get_kindergarten(db, kg_id)
    if not db_item:
        return None

    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_kindergarten(db: Session, kg_id: int):
    db_item = get_kindergarten(db, kg_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False


def create_review(db: Session, kg_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict(), kindergarten_id=kg_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review