#------------------------------------------------------------------------------
# Copyright 2014 Numenta Inc.
#
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
#------------------------------------------------------------------------------
from agent import AvogadroAgent
import os, csv

from model_params import getModelParams



class AvogadroKeyCountAgent(AvogadroAgent):
  name = "KeyCount"
  minVal = 0.0
  maxVal = 1000.0
  numBuckets = 284
  resolution = max(0.001, (maxVal - minVal) / numBuckets)

  ENCODER_PARAMS = {
    name: {
      "name": name,
      "fieldname": name,
      "resolution": resolution,
      "seed": 42,
      "type": "RandomDistributedScalarEncoder"
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    inPath = os.path.dirname(os.path.realpath(__file__)) + "/keys.temp"
    if os.path.isfile(inPath):
      with open(inPath, "rb") as inputFile:
        csvreader = csv.reader(inputFile)
        for row in csvreader:
          data = int(row[0])
          return data

class AvogadroKeyDownDownAgent(AvogadroAgent):
  name = "KeyDownDown"
  minVal = 0.0
  maxVal = 300.0
  numBuckets = 284
  resolution = max(0.001, (maxVal - minVal) / numBuckets)

  ENCODER_PARAMS = {
    name: {
      "name": name,
      "fieldname": name,
      "resolution": resolution,
      "seed": 42,
      "type": "RandomDistributedScalarEncoder"
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    inPath = os.path.dirname(os.path.realpath(__file__)) + "/keys.temp"
    if os.path.isfile(inPath):
      with open(inPath, "rb") as inputFile:
        csvreader = csv.reader(inputFile)
        for row in csvreader:
          data = float(row[1])
          return data

class AvogadroKeyUpDownAgent(AvogadroAgent):
  name = "KeyUpDown"
  minVal = 0.0
  maxVal = 300.0
  numBuckets = 284
  resolution = max(0.001, (maxVal - minVal) / numBuckets)

  ENCODER_PARAMS = {
    name: {
      "name": name,
      "fieldname": name,
      "resolution": resolution,
      "seed": 42,
      "type": "RandomDistributedScalarEncoder"
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    inPath = os.path.dirname(os.path.realpath(__file__)) + "/keys.temp"
    if os.path.isfile(inPath):
      with open(inPath, "rb") as inputFile:
        csvreader = csv.reader(inputFile)
        for row in csvreader:
          data = float(row[2])
          return data

class AvogadroKeyHoldAgent(AvogadroAgent):
  name = "KeyHold"
  minVal = 0.0
  maxVal = 2.0
  numBuckets = 284
  resolution = max(0.001, (maxVal - minVal) / numBuckets)

  ENCODER_PARAMS = {
    name: {
      "name": name,
      "fieldname": name,
      "resolution": resolution,
      "seed": 42,
      "type": "RandomDistributedScalarEncoder"
    }
  }

  MODEL_PARAMS = getModelParams(ENCODER_PARAMS, name)

  def collect(self):
    inPath = os.path.dirname(os.path.realpath(__file__)) + "/keys.temp"
    if os.path.isfile(inPath):
      with open(inPath, "rb") as inputFile:
        csvreader = csv.reader(inputFile)
        for row in csvreader:
          data = float(row[3])
          return data
