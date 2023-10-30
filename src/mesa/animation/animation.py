import time
import pygame as pg
from typing import Union


class Animation:
    def __init__(self):
        self.dynamic_objects: list[DynamicObject] = []

    def update(self):
        for dynamic_object in self.dynamic_objects:
            dynamic_object.update()


class DynamicObject:
    def __init__(
        self,
        animation_manager: Animation,
        animation_object: Union[float, pg.Vector2, pg.Vector3],
    ):
        self.linear_interpolation_position = None
        self.animation_manager = animation_manager
        self.animation_object = animation_object
        self.begin_animation_object = None
        self.animation_manager.dynamic_objects.append(self)
        self.begin_timestamp = time.time()
        self.current_timestamp = time.time()
        self.animation_object_difference = None
        self.animation_function = None
        self.animation_duration = 0
        self.target_animation_object = None
        self.animation_fired = False

    def get_value(self):
        return self.animation_object

    def begin_movement(self):
        if self.target_animation_object is None:
            return
        if self.current_timestamp > self.animation_duration:
            self.animation_object = self.target_animation_object
            self.animation_fired = False
        if self.animation_function:
            self.linear_interpolation_position = self.animation_function(
                self.current_timestamp / self.animation_duration
            )
            self.animation_object = (
                self.begin_animation_object
                + self.linear_interpolation_position * self.animation_object_difference
            )
        else:
            raise ValueError("No Animation Function was given.")

    def is_moving(self):
        return self.animation_fired

    def go_to(
        self,
        target: Union[float, pg.Vector2, pg.Vector3],
        duration: float,
        animation_function,
    ):
        self.animation_fired = True
        self.begin_timestamp = time.time()

        if isinstance(self.animation_object, Union[pg.Vector2, pg.Vector3]):
            self.begin_animation_object = self.animation_object.copy()
            self.target_animation_object = target.copy()
        else:
            self.begin_animation_object = self.animation_object
            self.target_animation_object = target
        self.animation_duration = duration
        self.animation_function = animation_function
        self.animation_object_difference = target - self.animation_object

    def update(self):
        if self.animation_fired:
            self.current_timestamp = (time.time() - self.begin_timestamp) * 100
            self.begin_movement()
