#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
# Copyright 2015 Tin Arm Engineering AB
# Copyright 2018 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Capacitated Vehicle Routing Problem (CVRP).

   This is a sample using the routing library python wrapper to solve a CVRP
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters.
"""

from __future__ import print_function
from collections import namedtuple
from six.moves import xrange
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

###########################
# Problem Data Definition #
###########################
# Vehicle declaration
Vehicle = namedtuple('Vehicle', ['capacity'])

# City block declaration
CityBlock = namedtuple('CityBlock', ['width', 'height'])

class DataProblem():
  """Stores the data for the problem"""
  def __init__(self):
    """Initializes the data for the problem"""
    # Locations in block unit
    locations = \
            [(4, 4), # depot
             (2, 0), (8, 0), # order location
             (0, 1), (1, 1),
             (5, 2), (7, 2),
             (3, 3), (6, 3),
             (5, 5), (8, 5),
             (1, 6), (2, 6),
             (3, 7), (6, 7),
             (0, 8), (7, 8)]
    # Compute locations in meters using the block dimension defined as follow
    # Manhattan average block: 750ft x 264ft -> 228m x 80m
    # here we use: 114m x 80m city block
    # src: https://nyti.ms/2GDoRIe "NY Times: Know Your distance"
    city_block = CityBlock(width=228/2, height=80)
    self._locations = [(loc[0] * city_block.width, loc[1] * city_block.height)
                       for loc in locations]

    self._demands = \
        [0, # depot
         1, 1, # 1, 2
         2, 4, # 3, 4
         2, 4, # 5, 6
         8, 8, # 7, 8
         1, 2, # 9,10
         1, 2, # 11,12
         4, 4, # 13, 14
         8, 8] # 15, 16

  @property
  def vehicle(self):
    """Gets a vehicle"""
    return Vehicle(capacity=15)

  @property
  def num_vehicles(self):
    """Gets number of vehicles"""
    return 4

  @property
  def locations(self):
    """Gets locations"""
    return self._locations

  @property
  def num_locations(self):
    """Gets number of locations"""
    return len(self.locations)

  @property
  def depot(self):
    """Gets depot location index"""
    return 0

  @property
  def demands(self):
    """Gets demands at each location"""
    return self._demands

#######################
# Problem Constraints #
#######################
def manhattan_distance(position_1, position_2):
  """Computes the Manhattan distance between two points"""
  return (
      abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1]))

class CreateDistanceEvaluator(object):  # pylint: disable=too-few-public-methods
  """Creates callback to return distance between points."""
  def __init__(self, data):
    """Initializes the distance matrix."""
    self._distances = {}

    # precompute distance between location to have distance callback in O(1)
    for from_node in xrange(data.num_locations):
      self._distances[from_node] = {}
      for to_node in xrange(data.num_locations):
        if from_node == to_node:
          self._distances[from_node][to_node] = 0
        else:
          self._distances[from_node][to_node] = (
              manhattan_distance(data.locations[from_node],
                                 data.locations[to_node]))

  def distance_evaluator(self, from_node, to_node):
    """Returns the manhattan distance between the two nodes"""
    return self._distances[from_node][to_node]

class CreateDemandEvaluator(object):  # pylint: disable=too-few-public-methods
  """Creates callback to get demands at each location."""

  def __init__(self, data):
    """Initializes the demand array."""
    self._demands = data.demands

  def demand_evaluator(self, from_node, to_node):
    """Returns the demand of the current node"""
    del to_node
    return self._demands[from_node]

def add_capacity_constraints(routing, data, demand_evaluator):
  """Adds capacity constraint"""
  capacity = 'Capacity'
  routing.AddDimension(
      demand_evaluator,
      0,  # null capacity slack
      data.vehicle.capacity,
      True,  # start cumul to zero
      capacity)

###########
# Printer #
###########
def print_solution(data, routing, assignment):
  """Prints assignment on console"""
  print('Objective: {}'.format(assignment.ObjectiveValue()))
  total_distance = 0
  total_load = 0
  capacity_dimension = routing.GetDimensionOrDie('Capacity')
  for vehicle_id in xrange(data.num_vehicles):
    index = routing.Start(vehicle_id)
    plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
    distance = 0
    while not routing.IsEnd(index):
      load_var = capacity_dimension.CumulVar(index)
      plan_output += ' {} Load({}) -> '.format(
          routing.IndexToNode(index),
          assignment.Value(load_var))
      previous_index = index
      index = assignment.Value(routing.NextVar(index))
      distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
    load_var = capacity_dimension.CumulVar(index)
    plan_output += ' {0} Load({1})\n'.format(
        routing.IndexToNode(index),
        assignment.Value(load_var))
    plan_output += 'Distance of the route: {}m\n'.format(distance)
    plan_output += 'Load of the route: {}\n'.format(assignment.Value(load_var))
    print(plan_output)
    total_distance += distance
    total_load += assignment.Value(load_var)
  print('Total Distance of all routes: {}m'.format(total_distance))
  print('Total Load of all routes: {}'.format(total_load))

########
# Main #
########
def main():
  """Entry point of the program"""
  # Instantiate the data problem.
  data = DataProblem()

  # Create Routing Model
  routing = pywrapcp.RoutingModel(
      data.num_locations,
      data.num_vehicles,
      data.depot)

  # Define weight of each edge
  distance_evaluator = CreateDistanceEvaluator(data).distance_evaluator
  routing.SetArcCostEvaluatorOfAllVehicles(distance_evaluator)
  # Add Capacity constraint
  demand_evaluator = CreateDemandEvaluator(data).demand_evaluator
  add_capacity_constraints(routing, data, demand_evaluator)

  # Setting first solution heuristic (cheapest addition).
  search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
  search_parameters.first_solution_strategy = (
      routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC) # pylint: disable=no-member
  # Solve the problem.
  assignment = routing.SolveWithParameters(search_parameters)
  print_solution(data, routing, assignment)

if __name__ == '__main__':
  main()
