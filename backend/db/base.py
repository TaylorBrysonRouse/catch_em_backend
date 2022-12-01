# base - file used to import all db models

from db.base_class import Base
from db.models.users import User
from db.models.lakes import Lake
from db.models.catches import Catch
from db.models.clarities import Clarity
from db.models.colors import Color
from db.models.clouds import Cloud
from db.models.weights import Weight
from db.models.baits import Bait