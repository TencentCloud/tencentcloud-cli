# -*- coding: utf-8 -*-
DESC = "memcached-2019-03-18"
INFO = {
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID组成的数组，数组下标从0开始"
      },
      {
        "name": "InstanceNames",
        "desc": "实例名称组成的数组，数组下标从0开始"
      },
      {
        "name": "Limit",
        "desc": "实例列表的大小，参数默认值100"
      },
      {
        "name": "Offset",
        "desc": "偏移量，取Limit整数倍"
      },
      {
        "name": "OrderBy",
        "desc": "枚举范围： AddTimeStamp, InstanceName, ProjectId"
      },
      {
        "name": "OrderType",
        "desc": "0倒序，1正序，默认倒序"
      },
      {
        "name": "ProjectIds",
        "desc": "项目ID组成的数组，数组下标从0开始"
      },
      {
        "name": "SearchKeys",
        "desc": "搜索关键词：支持实例ID、实例名称、完整IP"
      },
      {
        "name": "UniqSubnetIds",
        "desc": "子网ID数组，数组下标从0开始，如：subnet-fdj24n34j2"
      },
      {
        "name": "UniqVpcIds",
        "desc": "私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络，如：vpc-sad23jfdfk"
      },
      {
        "name": "Vips",
        "desc": "实例服务IP组成的数组，数组下标从0开始"
      }
    ],
    "desc": "获取Cmem实例列表"
  }
}