# Lint as: python2, python3
# Copyright 2019 Google LLC. All Rights Reserved.
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
"""A set of standard TFX Artifact types.

Note: the artifact definitions here are expected to change.
"""

from tfx.types.artifact import Artifact
from tfx.types.artifact import Property
from tfx.types.artifact import PropertyType

# Span for an artifact.
SPAN_PROPERTY = Property(type=PropertyType.INT)
# Comma separated of splits for an artifact. Empty string means artifact
# has no split.
SPLIT_NAMES_PROPERTY = Property(type=PropertyType.STRING)


class Examples(Artifact):
  TYPE_NAME = 'Examples'
  PROPERTIES = {
      'span': SPAN_PROPERTY,
      'split_names': SPLIT_NAMES_PROPERTY,
  }


class ExampleAnomalies(Artifact):
  TYPE_NAME = 'ExampleAnomalies'
  PROPERTIES = {
      'span': SPAN_PROPERTY,
      'split_names': SPLIT_NAMES_PROPERTY,
  }


class ExampleStatistics(Artifact):
  TYPE_NAME = 'ExampleStatistics'
  PROPERTIES = {
      'span': SPAN_PROPERTY,
      'split_names': SPLIT_NAMES_PROPERTY,
  }


class ExternalArtifact(Artifact):
  TYPE_NAME = 'ExternalArtifact'


class InferenceResult(Artifact):
  TYPE_NAME = 'InferenceResult'


class InfraBlessing(Artifact):
  TYPE_NAME = 'InfraBlessing'


class Model(Artifact):
  TYPE_NAME = 'Model'


class ModelBlessing(Artifact):
  TYPE_NAME = 'ModelBlessing'


class ModelEvaluation(Artifact):
  TYPE_NAME = 'ModelEvaluation'


class PushedModel(Artifact):
  TYPE_NAME = 'PushedModel'


class Schema(Artifact):
  TYPE_NAME = 'Schema'


class TransformGraph(Artifact):
  TYPE_NAME = 'TransformGraph'


# Still WIP and subject to change.
class HyperParameters(Artifact):
  TYPE_NAME = 'HyperParameters'
