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
      }
    ],
    "desc": "提供修改产品的名称和描述等信息的能力"
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
      }
    ],
    "desc": "根据设备产品ID、设备名称，获取设备上报的属性数据。"
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
      }
    ],
    "desc": "提供根据产品名称查找产品的能力"
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
  "DescribeDeviceDataHistory": {
    "params": [
      {
        "name": "MinTime",
        "desc": "区间开始时间"
      },
      {
        "name": "MaxTime",
        "desc": "区间结束时间"
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
        "desc": "属性字段名称"
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
  "CreateStudioProduct": {
    "params": [
      {
        "name": "ProductName",
        "desc": "产品名称"
      },
      {
        "name": "CategoryId",
        "desc": "产品分组模板ID"
      },
      {
        "name": "ProductType",
        "desc": "产品类型"
      },
      {
        "name": "EncryptionType",
        "desc": "加密类型"
      },
      {
        "name": "NetType",
        "desc": "连接类型"
      },
      {
        "name": "DataProtocol",
        "desc": "数据协议"
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
  "DeleteProject": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "提供删除某个项目的能力"
  },
  "DescribeStudioProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      }
    ],
    "desc": "提供查看茶品详细信息的能力，包括产品的ID、数据协议、认证类型等重要参数"
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
        "desc": "属性数据"
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
  }
}