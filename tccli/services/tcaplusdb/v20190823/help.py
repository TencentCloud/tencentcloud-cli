# -*- coding: utf-8 -*-
DESC = "tcaplusdb-2019-08-23"
INFO = {
  "ModifyAppPassword": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "需要修改密码的应用实例ID"
      },
      {
        "name": "OldPassword",
        "desc": "应用旧密码"
      },
      {
        "name": "OldPasswordExpireTime",
        "desc": "应用旧密码预期失效时间"
      },
      {
        "name": "NewPassword",
        "desc": "应用新密码"
      },
      {
        "name": "Mode",
        "desc": "更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式"
      }
    ],
    "desc": "修改指定AppInstanceId的实例密码，后台将在旧密码失效之前同时支持TcaplusDB SDK使用旧密码和新密码访问数据库。在旧密码失效之前不能提交新的密码修改请求，在旧密码失效之后不能提交修改旧密码过期时间的请求。"
  },
  "DescribeUinInWhitelist": {
    "params": [],
    "desc": "查询本用户是否在白名单中，控制是否能创建TDR类型的APP或表"
  },
  "DescribeTablesInRecycle": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待查询表所属应用实例ID"
      },
      {
        "name": "LogicZoneIds",
        "desc": "待查询表所属大区列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：TableName，TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "结果列表数量"
      }
    ],
    "desc": "查询回收站中的表详情"
  },
  "RollbackTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待回档表所在应用实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待回档表列表"
      },
      {
        "name": "RollbackTime",
        "desc": "待回档时间"
      },
      {
        "name": "Mode",
        "desc": "回档模式，支持：`KEYS`"
      }
    ],
    "desc": "表数据回档"
  },
  "CreateZone": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "大区所属应用实例ID"
      },
      {
        "name": "ZoneName",
        "desc": "大区名称，可以采用中文、英文或数字字符，长度不能超过30"
      },
      {
        "name": "LogicZoneId",
        "desc": "大区ID，可以由用户指定，但在同一个App内不能重复，如果不指定则采用自增的模式"
      }
    ],
    "desc": "在TcaplusDB应用下创建大区"
  },
  "DeleteIdlFiles": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "应用实例ID"
      },
      {
        "name": "IdlFiles",
        "desc": "待删除的IDL文件信息列表"
      }
    ],
    "desc": "指定应用ID和待删除IDL文件的信息，删除目标文件，如果文件正在被表关联则删除失败。"
  },
  "RecoverRecycleTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "表所在应用实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待恢复表信息"
      }
    ],
    "desc": "恢复回收站中，用户自行删除的表。对欠费待释放的表无效。"
  },
  "ModifyAppName": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "需要修改名称的应用实例ID"
      },
      {
        "name": "AppName",
        "desc": "需要修改的应用名称，需要URLEncode"
      }
    ],
    "desc": "修改指定的应用名称"
  },
  "DeleteApp": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待删除的应用实例ID"
      }
    ],
    "desc": "删除TcaplusDB应用实例，必须在应用实例所属所有资源（包括大区，表）都已经释放的情况下才会成功。"
  },
  "CreateTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待创建表所属应用实例ID"
      },
      {
        "name": "IdlFiles",
        "desc": "用户选定的建表IDL文件列表"
      },
      {
        "name": "SelectedTables",
        "desc": "待创建表信息列表"
      }
    ],
    "desc": "根据选择的IDL文件列表，批量创建表"
  },
  "ModifyTableQuotas": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "带扩缩容表所属应用实例ID"
      },
      {
        "name": "TableQuotas",
        "desc": "已选中待修改的表配额列表"
      }
    ],
    "desc": "表扩缩容"
  },
  "DescribeZones": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "大区所属应用实例ID"
      },
      {
        "name": "LogicZoneIds",
        "desc": "大区ID"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：ZoneName，ZoneId"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "大区列表大小"
      }
    ],
    "desc": "查询大区列表"
  },
  "DeleteZone": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "大区所属的应用实例ID"
      },
      {
        "name": "LogicZoneId",
        "desc": "大区ID"
      }
    ],
    "desc": "删除大区"
  },
  "DescribeApps": {
    "params": [
      {
        "name": "ApplicationIds",
        "desc": "指定查询的应用ID"
      },
      {
        "name": "Filters",
        "desc": "查询过滤条件"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "应用列表的大小，默认值20"
      }
    ],
    "desc": "查询TcaplusDB应用列表，包含应用详细信息。"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "查询TcaplusDB服务支持的地域列表"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "ApplicationIds",
        "desc": "需要查询任务所属的应用ID列表"
      },
      {
        "name": "TaskIds",
        "desc": "需要查询的任务ID列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：Content，TaskType, Operator, Time"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "任务列表大小"
      }
    ],
    "desc": "查询任务列表"
  },
  "ModifyZoneName": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "大区所属的应用实例ID"
      },
      {
        "name": "LogicZoneId",
        "desc": "待修改名称的大区ID"
      },
      {
        "name": "ZoneName",
        "desc": "新的大区名称"
      }
    ],
    "desc": "修改TcaplusDB大区名称"
  },
  "CreateApp": {
    "params": [
      {
        "name": "IdlType",
        "desc": "应用数据描述语言类型，如：`PROTO`，`TDR`或`MIX`"
      },
      {
        "name": "AppName",
        "desc": "应用名称，可使用中文或英文字符，长度在30个字符以内"
      },
      {
        "name": "VpcId",
        "desc": "应用所绑定的私有网络实例ID，形如：vpc-f49l6u0z"
      },
      {
        "name": "SubnetId",
        "desc": "应用所绑定的子网实例ID，形如：subnet-pxir56ns"
      },
      {
        "name": "Password",
        "desc": "应用访问密码，可使用英文和数字字符，长度为12~16个字符"
      }
    ],
    "desc": "本接口用于创建TcaplusDB应用"
  },
  "CompareIdlFiles": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待修改表所在应用实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待修改表列表"
      },
      {
        "name": "ExistingIdlFiles",
        "desc": "选中的已上传IDL文件列表，与NewIdlFiles必选其一"
      },
      {
        "name": "NewIdlFiles",
        "desc": "本次上传IDL文件列表，与ExistingIdlFiles必选其一"
      }
    ],
    "desc": "选中目标表，上传并校验改表文件，返回是否允许修改表结构"
  },
  "DescribeIdlFileInfos": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "文件所属应用实例ID"
      },
      {
        "name": "LogicZoneIds",
        "desc": "文件所属大区ID"
      },
      {
        "name": "IdlFileIds",
        "desc": "指定文件ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "文件列表大小"
      }
    ],
    "desc": "查询表描述文件详情"
  },
  "DeleteTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待删除表所在应用实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待删除表信息列表"
      }
    ],
    "desc": "根据指定的表信息删除目标表"
  },
  "ModifyTableMemos": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "表所属应用实例ID"
      },
      {
        "name": "TableMemos",
        "desc": "选定表详情列表"
      }
    ],
    "desc": "修改表备注信息"
  },
  "VerifyIdlFiles": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待加表的应用实例ID"
      },
      {
        "name": "LogicZoneId",
        "desc": "待加表的大区ID"
      },
      {
        "name": "ExistingIdlFiles",
        "desc": "曾经上传过的IDL文件信息列表，与NewIdlFiles至少有一者"
      },
      {
        "name": "NewIdlFiles",
        "desc": "待上传的IDL文件信息列表，与ExistingIdlFiles至少有一者"
      }
    ],
    "desc": "上传并校验加表文件，返回校验合法的表定义"
  },
  "ModifyTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待修改表所在应用实例ID"
      },
      {
        "name": "IdlFiles",
        "desc": "选中的改表IDL文件"
      },
      {
        "name": "SelectedTables",
        "desc": "待改表列表"
      }
    ],
    "desc": "根据用户选定的表定义IDL文件，批量修改指定的表"
  },
  "DescribeTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "待查询表所属应用实例ID"
      },
      {
        "name": "LogicZoneIds",
        "desc": "待查询表所属大区列表"
      },
      {
        "name": "SelectedTables",
        "desc": "待查询表信息列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：TableName，TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "结果列表数量"
      }
    ],
    "desc": "查询表详情"
  },
  "ClearTables": {
    "params": [
      {
        "name": "ApplicationId",
        "desc": "表所属应用实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待清理表信息列表"
      }
    ],
    "desc": "根据给定的表信息，清除表数据。"
  }
}