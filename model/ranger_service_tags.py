#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from apache_ranger.model.ranger_base             import *
from apache_ranger.model.ranger_service_resource import RangerServiceResource
from apache_ranger.model.ranger_tag              import RangerTag
from apache_ranger.model.ranger_tagdef           import RangerTagDef
from apache_ranger.utils                         import *


class RangerServiceTags(RangerBase):
    OP_SET     = 'set'     # set tags for the given serviceResources
    OP_DELETE  = 'delete'  # delete tags associated with the given serviceResources
    OP_REPLACE = 'replace' # replace all resources and tags in the given serviceName with the given serviceResources and tags

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        RangerBase.__init__(self, attrs)

        self.op               = non_null(attrs.get('op'), 'set')
        self.serviceName      = attrs.get('serviceName')
        self.tagDefinitions   = attrs.get('tagDefinitions')
        self.tags             = attrs.get('tags')
        self.serviceResources = attrs.get('serviceResources')
        self.resourceToTagIds = attrs.get('resourceToTagIds')
        self.tagVersion       = attrs.get('tagVersion')
        self.tagUpdateTime    = attrs.get('tagUpdateTime')

    def type_coerce_attrs(self):
        super(RangerServiceTags, self).type_coerce_attrs()

        self.tagDefinitions   = type_coerce_dict(self.tagDefinitions, RangerTagDef)
        self.tags             = type_coerce_dict(self.tags, RangerTag)
        self.serviceResources = type_coerce_list(self.serviceResources, RangerServiceResource)
