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
  "AddUser": {
    "params": [],
    "desc": "注册用户"
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
    "desc": "提供分页查询某个产品Id下设备信息的能力。"
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
    "desc": "获取用户在物联网套件所创建的所有产品信息。"
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
    "desc": "提供在指定的产品Id下删除一个设备的能力。"
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
    "desc": "提供下发控制指令到指定设备的能力。"
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
        "desc": "产品描述"
      },
      {
        "name": "AuthType",
        "desc": "产品鉴权类型（0：直连，1：动态令牌），推荐使用动态令牌"
      },
      {
        "name": "DataTemplate",
        "desc": "数据模版（json数组）"
      }
    ],
    "desc": "为用户提供创建某型号物联网产品的能力。"
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
        "desc": "Qos(目前QoS支持0与1)"
      }
    ],
    "desc": "提供向指定的Topic发布消息的能力。"
  },
  "GetDeviceStatuses": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceNames",
        "desc": "设备名称列表（单次限制1000个设备）"
      }
    ],
    "desc": "批量获取设备的当前状态，状态包括在线、离线或未激活状态。"
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
    "desc": "删除用户指定的产品Id对应的信息。"
  },
  "AppAddUser": {
    "params": [
      {
        "name": "UserName",
        "desc": "用户名"
      },
      {
        "name": "Password",
        "desc": "密码"
      }
    ],
    "desc": "注册应用用户"
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
    "desc": "提供查询某个设备详细信息的能力。"
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
        "desc": "设备名称，唯一标识某产品下的一个设备"
      }
    ],
    "desc": "提供在指定的产品Id下创建一个设备的能力，生成设备名称与设备秘钥。"
  },
  "GetProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品Id"
      }
    ],
    "desc": "获取产品定义的详细信息，包括产品名称、产品描述，鉴权模式等信息。"
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
      },
      {
        "name": "DataTemplate",
        "desc": "数据模版（json）"
      }
    ],
    "desc": "提供修改产品信息及数据模板的能力。"
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
  }
}