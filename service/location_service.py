from helper.exception_handler import exception_handler
from schema.locationSchema import LocationModel
from repo.location_repo import locationRepo
from models.location import Location
from schema.response import ResponseModel
from sqlalchemy.orm import Session


class LocationService:
    def __init__(self, db_connection: Session):
        self.location_repo = locationRepo(db_connection)

    @exception_handler
    def add_location(self, location_data: LocationModel) -> ResponseModel:
        location = Location(**location_data.dict())
        added_location = self.location_repo.add_location(location)
        return ResponseModel(success=True, message="Location added successfully", data={"location": added_location})

    @exception_handler
    def delete_location(self, location_id: str) -> ResponseModel:
        self.location_repo.delete_location(location_id)
        return ResponseModel(success=True, message="Location deleted successfully")

    @exception_handler
    def get_location_by_id(self, location_id: str) -> ResponseModel:
        location = self.location_repo.get_location_by_id(location_id)
        if not location:
            return ResponseModel(success=False, message="Location not found")
        return ResponseModel(success=True, message="Location retrieved successfully", data={"location": location})

    @exception_handler
    def get_all_locations(self) -> ResponseModel:
        locations = self.location_repo.get_all_locations()
        if locations is None:
            return ResponseModel(success=False, message="No locations found")
        return ResponseModel(success=True, message="Locations retrieved successfully", data={"locations": locations})

    @exception_handler
    def update_location(self, location_id: str, location_data: LocationModel) -> ResponseModel:
        existing_location = self.location_repo.get_location_by_id(location_id)
        if not existing_location:
            return ResponseModel(success=False, message="Location not found")

        for key, value in location_data.dict().items():
            setattr(existing_location, key, value)

        updated_location = self.location_repo.update_location(
            existing_location)
        return ResponseModel(success=True, message="Location updated successfully", data={"location": updated_location})
