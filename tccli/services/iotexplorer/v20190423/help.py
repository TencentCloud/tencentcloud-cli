# -*- coding: utf-8 -*-
DESC = "iotexplorer-2019-04-23"
INFO = {
  "ModifyStudioProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "ProductName",
        "desc": "产品名称"
      },
      {
        "name": "ProductDesc",
        "desc": "产品描述"
      },
      {
        "name": "ModuleId",
        "desc": "模型ID"
      },
      {
        "name": "EnableProductScript",
        "desc": "是否打开二进制转Json功能, 取值为字符串 true/false"
      }
    ],
    "desc": "提供修改产品的名称和描述等信息的能力，对于已发布产品不允许进行修改。"
  },
  "DeleteStudioProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "提供删除某个项目下产品的能力"
  },
  "DescribeDeviceData": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "DeviceId",
        "desc": "设备ID，该字段有值将代替 ProductId/DeviceName"
      }
    ],
    "desc": "根据设备产品ID、设备名称，获取设备上报的属性数据。"
  },
  "DeleteLoRaGateway": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "LoRa 网关 Id"
      }
    ],
    "desc": "删除  LoRa 网关的接口"
  },
  "CreateStudioProduct": {
    "params": [
      {
        "name": "ProductName",
        "desc": "产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}"
      },
      {
        "name": "CategoryId",
        "desc": "产品分组模板ID , ( 自定义模板填写1 , 控制台调用会使用预置的其他ID)"
      },
      {
        "name": "ProductType",
        "desc": "产品类型 填写 ( 0 普通产品 )"
      },
      {
        "name": "EncryptionType",
        "desc": "加密类型 加密类型，1表示证书认证，2表示签名认证。"
      },
      {
        "name": "NetType",
        "desc": "连接类型 可以填写 wifi cellular else"
      },
      {
        "name": "DataProtocol",
        "desc": "数据协议 (1 使用物模型 2 为自定义)"
      },
      {
        "name": "ProductDesc",
        "desc": "产品描述"
      },
      {
        "name": "ProjectId",
        "desc": "产品的项目ID"
      }
    ],
    "desc": "为用户提供新建产品的能力，用于管理用户的设备"
  },
  "DescribeDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名"
      },
      {
        "name": "DeviceId",
        "desc": "设备ID，该字段有值将代替 ProductId/DeviceName"
      }
    ],
    "desc": "用于查看某个设备的详细信息"
  },
  "CreateLoRaGateway": {
    "params": [
      {
        "name": "GatewayId",
        "desc": "LoRa 网关Id"
      },
      {
        "name": "Name",
        "desc": "网关名称"
      },
      {
        "name": "Description",
        "desc": "详情描述"
      },
      {
        "name": "Location",
        "desc": "位置坐标"
      },
      {
        "name": "Position",
        "desc": "位置信息"
      },
      {
        "name": "PositionDetails",
        "desc": "位置详情"
      },
      {
        "name": "IsPublic",
        "desc": "是否公开"
      }
    ],
    "desc": "创建新 LoRa 网关设备接口"
  },
  "CallDeviceActionAsync": {
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
        "name": "ActionId",
        "desc": "产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义"
      },
      {
        "name": "InputParams",
        "desc": "输入参数"
      }
    ],
    "desc": "提供给用户异步调用设备行为的能力"
  },
  "SearchStudioProduct": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "ProductName",
        "desc": "产品名称"
      },
      {
        "name": "Limit",
        "desc": "列表Limit"
      },
      {
        "name": "Offset",
        "desc": "列表Offset"
      },
      {
        "name": "DevStatus",
        "desc": "产品Status"
      }
    ],
    "desc": "提供根据产品名称查找产品的能力"
  },
  "GetProjectList": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "个数限制"
      }
    ],
    "desc": "提供查询用户所创建的项目列表查询功能。"
  },
  "DescribeDeviceDataHistory": {
    "params": [
      {
        "name": "MinTime",
        "desc": "区间开始时间（Unix 时间戳，毫秒级）"
      },
      {
        "name": "MaxTime",
        "desc": "区间结束时间（Unix 时间戳，毫秒级）"
      },
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "FieldName",
        "desc": "属性字段名称，对应数据模板中功能属性的标识符"
      },
      {
        "name": "Limit",
        "desc": "返回条数"
      },
      {
        "name": "Context",
        "desc": "检索上下文"
      }
    ],
    "desc": "获取设备在指定时间范围内上报的历史数据。"
  },
  "CallDeviceActionSync": {
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
        "name": "ActionId",
        "desc": "产品数据模板中行为功能的标识符，由开发者自行根据设备的应用场景定义"
      },
      {
        "name": "InputParams",
        "desc": "输入参数"
      }
    ],
    "desc": "为用户提供同步调用设备行为的能力。"
  },
  "DeleteDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID。"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称。"
      }
    ],
    "desc": "删除设备"
  },
  "ModifyProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "ProjectName",
        "desc": "项目名称"
      },
      {
        "name": "ProjectDesc",
        "desc": "项目描述"
      }
    ],
    "desc": "修改项目"
  },
  "GetDeviceList": {
    "params": [
      {
        "name": "ProductId",
        "desc": "需要查看设备列表的产品 ID"
      },
      {
        "name": "Offset",
        "desc": "分页偏移"
      },
      {
        "name": "Limit",
        "desc": "分页的大小，数值范围 10-100"
      }
    ],
    "desc": "用于查询某个产品下的设备列表"
  },
  "CreateDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID。"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。"
      },
      {
        "name": "DevAddr",
        "desc": "LoRaWAN 设备地址"
      },
      {
        "name": "AppKey",
        "desc": "LoRaWAN 应用密钥"
      },
      {
        "name": "DevEUI",
        "desc": "LoRaWAN 设备唯一标识"
      },
      {
        "name": "AppSKey",
        "desc": "LoRaWAN 应用会话密钥"
      },
      {
        "name": "NwkSKey",
        "desc": "LoRaWAN 网络会话密钥"
      }
    ],
    "desc": "创建设备"
  },
  "ListEventHistory": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "Type",
        "desc": "搜索的事件类型：alert 表示告警，fault 表示故障，info 表示信息，为空则表示查询上述所有类型事件"
      },
      {
        "name": "StartTime",
        "desc": "起始时间（Unix 时间戳，秒级）, 为0 表示 当前时间 - 24h"
      },
      {
        "name": "EndTime",
        "desc": "结束时间（Unix 时间戳，秒级）, 为0 表示当前时间"
      },
      {
        "name": "Context",
        "desc": "搜索上下文, 用作查询游标"
      },
      {
        "name": "Size",
        "desc": "单次获取的历史数据项目的最大数量"
      }
    ],
    "desc": "获取设备的历史事件"
  },
  "DescribeStudioProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "提供查看产品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数"
  },
  "GetLoRaGatewayList": {
    "params": [
      {
        "name": "IsCommunity",
        "desc": "是否是社区网关"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "限制个数"
      }
    ],
    "desc": "获取 LoRa 网关列表接口"
  },
  "ReleaseStudioProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DevStatus",
        "desc": "产品DevStatus"
      }
    ],
    "desc": "产品开发完成并测试通过后，通过发布产品将产品设置为发布状态"
  },
  "ModifyModelDefinition": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "ModelSchema",
        "desc": "数据模板定义"
      }
    ],
    "desc": "提供修改产品的数据模板的能力"
  },
  "DescribeProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "查询项目详情"
  },
  "DescribeModelDefinition": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "查询产品配置的数据模板信息"
  },
  "CreateProject": {
    "params": [
      {
        "name": "ProjectName",
        "desc": "项目名称"
      },
      {
        "name": "ProjectDesc",
        "desc": "项目描述"
      }
    ],
    "desc": "为用户提供新建项目的能力，用于集中管理产品和应用。"
  },
  "ModifyLoRaGateway": {
    "params": [
      {
        "name": "Description",
        "desc": "描述信息"
      },
      {
        "name": "GatewayId",
        "desc": "LoRa网关Id"
      },
      {
        "name": "Location",
        "desc": "LoRa网关位置坐标"
      },
      {
        "name": "Name",
        "desc": "LoRa网关名称"
      },
      {
        "name": "IsPublic",
        "desc": "是否公开可见"
      },
      {
        "name": "Position",
        "desc": "位置信息"
      },
      {
        "name": "PositionDetails",
        "desc": "位置详情"
      }
    ],
    "desc": "修改 LoRa 网关信息"
  },
  "DeleteProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "提供删除某个项目的能力"
  },
  "ControlDeviceData": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "Data",
        "desc": "属性数据, JSON格式字符串, 注意字段需要在物模型属性里定义"
      },
      {
        "name": "Method",
        "desc": "请求类型 , 不填该参数或者 desired 表示下发属性给设备,  reported 表示模拟设备上报属性"
      },
      {
        "name": "DeviceId",
        "desc": "设备ID，该字段有值将代替 ProductId/DeviceName , 通常情况不需要填写"
      },
      {
        "name": "DataTimestamp",
        "desc": "上报数据UNIX时间戳(毫秒), 仅对Method:reported有效"
      }
    ],
    "desc": "根据设备产品ID、设备名称，设置控制设备的属性数据。"
  },
  "GetStudioProductList": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      },
      {
        "name": "DevStatus",
        "desc": "产品DevStatus"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      }
    ],
    "desc": "提供查询某个项目下所有产品信息的能力。"
  }
}