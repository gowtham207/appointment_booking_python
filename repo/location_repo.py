from sqlalchemy.orm import Session
from models.location import Location


class locationRepo:

    def __init__(self, db_connection: Session):
        self.db_connection = db_connection

    def add_location(self, location_data: Location) -> Location:
        self.db_connection.add(location_data)
        self.db_connection.commit()
        self.db_connection.refresh(location_data)
        return location_data

    def update_location(self, location: Location) -> Location:
        updated_location = self.db_connection.merge(location)
        self.db_connection.commit()
        self.db_connection.refresh(updated_location)
        return updated_location

    def get_location_by_id(self, location_id: str) -> Location:
        return self.db_connection.query(Location).filter(
            Location.id == location_id,
            Location.deleted_at.is_(None)
        ).first()

    def delete_location(self, location: Location) -> Location:
        location.deleted_at = datetime.utcnow()
        deleted_location = self.db_connection.merge(location)
        self.db_connection.commit()
        self.db_connection.refresh(deleted_location)
        return deleted_location

    def get_all_locations(self) -> list[Location]:
        return self.db_connection.query(Location).filter(
            Location.deleted_at.is_(None)
        ).all()
