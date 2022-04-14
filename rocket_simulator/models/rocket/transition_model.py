from dataclasses import dataclass

from material_model import MaterialModel
from models.physics.rigid_body import RigidBody

class TransitionModel:
    def __init__(self, position, height, bottom_diameter, top_diameter, thickness, material):
        self.__position = position
        self.__height = height
        self.__bottom_diameter = bottom_diameter
        self.__top_diameter = top_diameter
        self.__thickness = thickness
        self.__material = material
        self.__rigid_body = self.__createRigidBody()
        
    def __createRigidBody():
        pass