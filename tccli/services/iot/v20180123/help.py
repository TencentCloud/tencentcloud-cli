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
        "desc": "设备名称列表，允许最多一次100台"
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
    "desc": "批量获取设备某一段时间范围的设备上报数据。该接口只允许使用数据模板类型的产品通过REST API方式同步设备上报数据至用户的应用系统。"
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
    "desc": "重置设备操作，将会为设备生成新的证书及清空最新数据，需谨慎操作。"
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
    "desc": "新增Topic，用于设备或应用发布消息至该Topic或订阅该Topic的消息。"
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
    "desc": "提供下发控制指令到指定设备的能力，该接口适用于使用数据模板类型的产品。"
  },
  "GetUser": {
    "params": [],
    "desc": "获取用户信息"
  },
  "AddProduct": {
    "params": [
      {
        "name": "Name",
        "desc": "产品名称，同一区域产品名称需唯一，支持中文、英文字母、中划线和下划线，长度不超过31个字符，中文占两个字符"
      },
      {
        "name": "Description",
        "desc": "产品描述"
      },
      {
        "name": "AuthType",
        "desc": "鉴权模式（1：动态令牌，推荐使用动态令牌）"
      },
      {
        "name": "DataTemplate",
        "desc": "数据模版（json数组）"
      },
      {
        "name": "DataProtocol",
        "desc": "数据协议（native表示自定义，template表示数据模板，默认值为template）"
      }
    ],
    "desc": "本接口(AddProduct)用于创建、定义某款硬件产品。"
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
    "desc": "提供向指定的Topic发布消息的能力，常用于向设备下发控制指令；该接口只适用于数据协议为“自定义”类型的产品，使用数据模板类型的产品需使用IssueDeviceControl接口"
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
    "desc": "获取某个设备当前上报到云端的数据，该接口适用于使用数据模板协议的产品。"
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
        "desc": "设备名称列表，最大支持100台"
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
      },
      {
        "name": "Type",
        "desc": "日志类型（comm/status）"
      }
    ],
    "desc": "批量获取设备与云端的详细通信日志，该接口适用于使用数据模板类型的产品。"
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