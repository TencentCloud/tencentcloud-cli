# -*- coding: utf-8 -*-
DESC = "iot-2018-01-23"
INFO = {
  "GetDataHistory": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceNames",
        "desc": "设备名称列表"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "Size",
        "desc": "查询数据量"
      },
      {
        "name": "Order",
        "desc": "时间排序（desc/asc）"
      },
      {
        "name": "ScrollId",
        "desc": "查询游标"
      }
    ],
    "desc": "获取数据历史"
  },
  "ResetDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "重置设备"
  },
  "DeactivateRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      }
    ],
    "desc": "禁用规则"
  },
  "GetDevices": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Length",
        "desc": "长度"
      }
    ],
    "desc": "获取设备列表"
  },
  "AddTopic": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "TopicName",
        "desc": "Topic名称"
      }
    ],
    "desc": "新增Topic"
  },
  "GetProducts": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Length",
        "desc": "长度"
      }
    ],
    "desc": "获取用户名下的产品列表"
  },
  "DeleteDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "删除设备"
  },
  "AddRule": {
    "params": [
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "Description",
        "desc": "描述"
      },
      {
        "name": "Query",
        "desc": "查询"
      },
      {
        "name": "Actions",
        "desc": "转发"
      }
    ],
    "desc": "新增规则"
  },
  "DeleteRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      }
    ],
    "desc": "删除规则"
  },
  "IssueDeviceControl": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "ControlData",
        "desc": "控制数据（json）"
      }
    ],
    "desc": "下发设备控制指令"
  },
  "GetUser": {
    "params": [],
    "desc": "获取用户信息"
  },
  "AddProduct": {
    "params": [
      {
        "name": "Name",
        "desc": "产品名称"
      },
      {
        "name": "Description",
        "desc": "产品类型"
      },
      {
        "name": "AuthType",
        "desc": "产品鉴权类型（0：直连，1：Token）"
      },
      {
        "name": "DataTemplate",
        "desc": "数据模版（json数组）"
      }
    ],
    "desc": "新增产品"
  },
  "UpdateRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      },
      {
        "name": "Name",
        "desc": "名称"
      },
      {
        "name": "Description",
        "desc": "描述"
      },
      {
        "name": "Query",
        "desc": "查询"
      },
      {
        "name": "Actions",
        "desc": "转发"
      }
    ],
    "desc": "更新规则"
  },
  "PublishMsg": {
    "params": [
      {
        "name": "Topic",
        "desc": "Topic"
      },
      {
        "name": "Message",
        "desc": "消息内容"
      },
      {
        "name": "Qos",
        "desc": "Qos"
      }
    ],
    "desc": "向Topic发布消息"
  },
  "GetDeviceStatuses": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceNames",
        "desc": "设备名称列表（单次限制1000个）"
      }
    ],
    "desc": "批量获取设备状态"
  },
  "GetRules": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Length",
        "desc": "长度"
      }
    ],
    "desc": "获取转发规则列表"
  },
  "DeleteProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      }
    ],
    "desc": "删除产品"
  },
  "GetTopic": {
    "params": [
      {
        "name": "TopicId",
        "desc": "TopicId"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      }
    ],
    "desc": "获取Topic信息"
  },
  "GetDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "获取设备信息"
  },
  "GetDeviceData": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "获取设备数据"
  },
  "GetRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      }
    ],
    "desc": "获取转发规则信息"
  },
  "GetDeviceLog": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceNames",
        "desc": "设备名称列表"
      },
      {
        "name": "StartTime",
        "desc": "查询开始时间"
      },
      {
        "name": "EndTime",
        "desc": "查询结束时间"
      },
      {
        "name": "Size",
        "desc": "查询数据量"
      },
      {
        "name": "Order",
        "desc": "时间排序（desc/asc）"
      },
      {
        "name": "ScrollId",
        "desc": "查询游标"
      }
    ],
    "desc": "获取设备日志"
  },
  "GetTopics": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Length",
        "desc": "长度"
      }
    ],
    "desc": "获取Topic列表"
  },
  "AddDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "新增设备"
  },
  "GetProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      }
    ],
    "desc": "获取产品信息"
  },
  "UpdateProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "Name",
        "desc": "产品名称"
      },
      {
        "name": "Description",
        "desc": "产品描述"
      }
    ],
    "desc": "更新产品信息"
  },
  "ActivateRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      }
    ],
    "desc": "启用规则"
  },
  "DeleteTopic": {
    "params": [
      {
        "name": "TopicId",
        "desc": "TopicId"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      }
    ],
    "desc": "删除Topic"
  }
}