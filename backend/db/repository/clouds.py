from sqlalchemy.orm import Session
from db.models.clouds import Cloud

# clouds - file used for handling cloud type methods that touch the db
def get_cloud_type(cloud_percent, db: Session):
  cloud_types = db.query(Cloud).all()

  for i in cloud_types:
    if i.cloud_type_range_min <= cloud_percent <= i.cloud_type_range_max:
      cloud_type_id = i.id
  
  return cloud_type_id