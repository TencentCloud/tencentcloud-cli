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
    "desc": "批量获取设备某一段时间范围的设备上报数据。该接口适用于使用高级版类型的产品"
  },
  "AppSecureAddDevice": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "DeviceSignature",
        "desc": "设备签名"
      }
    ],
    "desc": "用户绑定设备，绑定后可以在APP端进行控制。绑定设备前需调用“获取设备绑定签名”接口"
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
      },
      {
        "name": "Keyword",
        "desc": "关键字查询"
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
  "AppGetDeviceStatuses": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "DeviceIds",
        "desc": "设备Id列表（单次限制1000个设备）"
      }
    ],
    "desc": "获取绑定设备的上下线状态"
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
  "AppGetToken": {
    "params": [
      {
        "name": "UserName",
        "desc": "用户名"
      },
      {
        "name": "Password",
        "desc": "密码"
      },
      {
        "name": "Expire",
        "desc": "TTL"
      }
    ],
    "desc": "获取用户token"
  },
  "AppUpdateUser": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "NickName",
        "desc": "昵称"
      }
    ],
    "desc": "修改用户信息"
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
  "ActivateRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "规则Id"
      }
    ],
    "desc": "启用规则"
  },
  "GetDeviceStatistics": {
    "params": [
      {
        "name": "Products",
        "desc": "产品Id列表"
      },
      {
        "name": "StartDate",
        "desc": "开始日期"
      },
      {
        "name": "EndDate",
        "desc": "结束日期"
      }
    ],
    "desc": "查询某段时间范围内产品的在线、激活设备数"
  },
  "UnassociateSubDeviceFromGatewayProduct": {
    "params": [
      {
        "name": "SubDeviceProductId",
        "desc": "子设备产品Id"
      },
      {
        "name": "GatewayProductId",
        "desc": "网关设备产品Id"
      }
    ],
    "desc": "取消子设备产品与网关设备产品的关联"
  },
  "AppResetPassword": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "OldPassword",
        "desc": "旧密码"
      },
      {
        "name": "NewPassword",
        "desc": "新密码"
      }
    ],
    "desc": "重置APP用户密码"
  },
  "GetDeviceSignatures": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceNames",
        "desc": "设备名称列表（单次限制1000个设备）"
      },
      {
        "name": "Expire",
        "desc": "过期时间"
      }
    ],
    "desc": "获取设备绑定签名，用于用户绑定某个设备的应用场景"
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
  "AppGetDeviceData": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "获取绑定设备数据，用于实时展示设备的最新数据"
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
        "name": "DataTemplate",
        "desc": "数据模版"
      },
      {
        "name": "DataProtocol",
        "desc": "产品版本（native表示基础版，template表示高级版，默认值为template）"
      },
      {
        "name": "AuthType",
        "desc": "设备认证方式（1：动态令牌，2：签名直连鉴权）"
      },
      {
        "name": "CommProtocol",
        "desc": "通信方式（other/wifi/cellular/nb-iot）"
      },
      {
        "name": "DeviceType",
        "desc": "产品的设备类型（device: 直连设备；sub_device：子设备；gateway：网关设备）"
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
        "desc": "转发动作列表"
      },
      {
        "name": "DataType",
        "desc": "数据类型（0：文本，1：二进制）"
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
    "desc": "提供向指定的Topic发布消息的能力，常用于向设备下发控制指令。该接口只适用于产品版本为“基础版”类型的产品，使用高级版的产品需使用“下发设备控制指令”接口"
  },
  "GetDebugLog": {
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
        "desc": "日志类型（shadow/action/mqtt）"
      }
    ],
    "desc": "获取设备的调试日志，用于定位问题"
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
      },
      {
        "name": "Metadata",
        "desc": "是否发送metadata字段"
      }
    ],
    "desc": "提供下发控制指令到指定设备的能力，该接口适用于使用高级版类型的产品。"
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
  "AppGetUser": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      }
    ],
    "desc": "获取用户信息"
  },
  "AppGetDevices": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      }
    ],
    "desc": "获取用户的绑定设备列表"
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
    "desc": "为APP提供用户注册功能"
  },
  "AppIssueDeviceControl": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
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
      },
      {
        "name": "Metadata",
        "desc": "是否发送metadata字段"
      }
    ],
    "desc": "用户通过APP控制设备"
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
  "AppDeleteDevice": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "用户解除与设备的关联关系，解除后APP用户无法控制设备，获取设备数据"
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
  "AppGetDevice": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      }
    ],
    "desc": "获取绑定设备的基本信息与数据模板定义"
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
    "desc": "批量获取设备与云端的详细通信日志，该接口适用于使用高级版类型的产品。"
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
        "desc": "数据模版"
      }
    ],
    "desc": "提供修改产品信息及数据模板的能力。"
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
        "desc": "转发动作列表"
      },
      {
        "name": "DataType",
        "desc": "数据类型（0：文本，1：二进制）"
      }
    ],
    "desc": "新增规则"
  },
  "AssociateSubDeviceToGatewayProduct": {
    "params": [
      {
        "name": "SubDeviceProductId",
        "desc": "子设备产品Id"
      },
      {
        "name": "GatewayProductId",
        "desc": "网关产品Id"
      }
    ],
    "desc": "关联子设备产品和网关产品"
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
  "AppUpdateDevice": {
    "params": [
      {
        "name": "AccessToken",
        "desc": "访问Token"
      },
      {
        "name": "ProductId",
        "desc": "产品Id"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "AliasName",
        "desc": "设备别名"
      }
    ],
    "desc": "修改设备别名，便于用户个性化定义设备的名称"
  }
}