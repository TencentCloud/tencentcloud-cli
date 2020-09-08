# -*- coding: utf-8 -*-
DESC = "tcaplusdb-2019-08-23"
INFO = {
  "DeleteTableIndex": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格所属集群实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待删除分布式索引的表格列表"
      }
    ],
    "desc": "删除表格的分布式索引"
  },
  "DescribeTableTags": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格所属集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "表格列表"
      }
    ],
    "desc": "获取表格标签"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "需要查询任务所属的集群ID列表"
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
        "desc": "查询列表偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询列表返回记录数"
      }
    ],
    "desc": "查询任务列表"
  },
  "CreateCluster": {
    "params": [
      {
        "name": "IdlType",
        "desc": "集群数据描述语言类型，如：`PROTO`，`TDR`或`MIX`"
      },
      {
        "name": "ClusterName",
        "desc": "集群名称，可使用中文或英文字符，最大长度32个字符"
      },
      {
        "name": "VpcId",
        "desc": "集群所绑定的私有网络实例ID，形如：vpc-f49l6u0z"
      },
      {
        "name": "SubnetId",
        "desc": "集群所绑定的子网实例ID，形如：subnet-pxir56ns"
      },
      {
        "name": "Password",
        "desc": "集群访问密码，必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母"
      },
      {
        "name": "ResourceTags",
        "desc": "集群标签列表"
      },
      {
        "name": "Ipv6Enable",
        "desc": "集群是否开启IPv6功能"
      }
    ],
    "desc": "本接口用于创建TcaplusDB集群"
  },
  "DescribeUinInWhitelist": {
    "params": [],
    "desc": "查询本用户是否在白名单中，控制是否能创建TDR类型的APP或表"
  },
  "DescribeTablesInRecycle": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待查询表格所属集群ID"
      },
      {
        "name": "TableGroupIds",
        "desc": "待查询表格所属表格组ID列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：TableName，TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "查询结果偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询结果返回记录数量"
      }
    ],
    "desc": "查询回收站中的表详情"
  },
  "RollbackTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待回档表格所在集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待回档表格列表"
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
    "desc": "表格数据回档"
  },
  "ModifyClusterName": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "需要修改名称的集群ID"
      },
      {
        "name": "ClusterName",
        "desc": "需要修改的集群名称，可使用中文或英文字符，最大长度32个字符"
      }
    ],
    "desc": "修改指定的集群名称"
  },
  "DeleteCluster": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待删除的集群ID"
      }
    ],
    "desc": "删除TcaplusDB集群，必须在集群所属所有资源（包括表格组，表）都已经释放的情况下才会成功。"
  },
  "ModifyClusterPassword": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "需要修改密码的集群ID"
      },
      {
        "name": "OldPassword",
        "desc": "集群旧密码"
      },
      {
        "name": "OldPasswordExpireTime",
        "desc": "集群旧密码预期失效时间"
      },
      {
        "name": "NewPassword",
        "desc": "集群新密码，密码必须是a-zA-Z0-9的字符,且必须包含数字和大小写字母"
      },
      {
        "name": "Mode",
        "desc": "更新模式： `1` 更新密码；`2` 更新旧密码失效时间，默认为`1` 模式"
      }
    ],
    "desc": "修改指定集群的密码，后台将在旧密码失效之前同时支持TcaplusDB SDK使用旧密码和新密码访问数据库。在旧密码失效之前不能提交新的密码修改请求，在旧密码失效之后不能提交修改旧密码过期时间的请求。"
  },
  "DeleteIdlFiles": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "IDL所属集群ID"
      },
      {
        "name": "IdlFiles",
        "desc": "待删除的IDL文件信息列表"
      }
    ],
    "desc": "指定集群ID和待删除IDL文件的信息，删除目标文件，如果文件正在被表关联则删除失败。"
  },
  "RecoverRecycleTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表所在集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待恢复表信息"
      }
    ],
    "desc": "恢复回收站中，用户自行删除的表。对欠费待释放的表无效。"
  },
  "SetTableIndex": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表所属集群实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待创建分布式索引表格列表"
      }
    ],
    "desc": "设置表格分布式索引"
  },
  "CreateBackup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待创建备份表所属集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待创建备份表信息列表"
      },
      {
        "name": "Remark",
        "desc": "备注信息"
      }
    ],
    "desc": "用户创建备份任务"
  },
  "CreateTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待创建表格所属集群ID"
      },
      {
        "name": "IdlFiles",
        "desc": "用户选定的建表格IDL文件列表"
      },
      {
        "name": "SelectedTables",
        "desc": "待创建表格信息列表"
      },
      {
        "name": "ResourceTags",
        "desc": "表格标签列表"
      }
    ],
    "desc": "根据选择的IDL文件列表，批量创建表格"
  },
  "ModifyTableQuotas": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "带扩缩容表所属集群ID"
      },
      {
        "name": "TableQuotas",
        "desc": "已选中待修改的表配额列表"
      }
    ],
    "desc": "表格扩缩容"
  },
  "DescribeClusters": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "指定查询的集群ID列表"
      },
      {
        "name": "Filters",
        "desc": "查询过滤条件"
      },
      {
        "name": "Offset",
        "desc": "查询列表偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询列表返回记录数，默认值20"
      },
      {
        "name": "Ipv6Enable",
        "desc": "是否启用Ipv6"
      }
    ],
    "desc": "查询TcaplusDB集群列表，包含集群详细信息。"
  },
  "DeleteTableGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格组所属的集群ID"
      },
      {
        "name": "TableGroupId",
        "desc": "表格组ID"
      }
    ],
    "desc": "删除表格组"
  },
  "ModifyTableGroupName": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格组所属的集群ID"
      },
      {
        "name": "TableGroupId",
        "desc": "待修改名称的表格组ID"
      },
      {
        "name": "TableGroupName",
        "desc": "新的表格组名称，可以使用中英文字符和符号"
      }
    ],
    "desc": "修改TcaplusDB表格组名称"
  },
  "CreateTableGroup": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格组所属集群ID"
      },
      {
        "name": "TableGroupName",
        "desc": "表格组名称，可以采用中文、英文或数字字符，最大长度32个字符"
      },
      {
        "name": "TableGroupId",
        "desc": "表格组ID，可以由用户指定，但在同一个集群内不能重复，如果不指定则采用自增的模式"
      },
      {
        "name": "ResourceTags",
        "desc": "表格组标签列表"
      }
    ],
    "desc": "在TcaplusDB集群下创建表格组"
  },
  "DescribeRegions": {
    "params": [],
    "desc": "查询TcaplusDB服务支持的地域列表"
  },
  "ModifyTableTags": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待修改标签表格所属集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待修改标签表格列表"
      },
      {
        "name": "ReplaceTags",
        "desc": "待增加或修改的标签列表"
      },
      {
        "name": "DeleteTags",
        "desc": "待删除的标签列表"
      }
    ],
    "desc": "修改表格标签"
  },
  "ModifyClusterTags": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待修改标签的集群ID"
      },
      {
        "name": "ReplaceTags",
        "desc": "待增加或修改的标签列表"
      },
      {
        "name": "DeleteTags",
        "desc": "待删除的标签"
      }
    ],
    "desc": "修改集群标签"
  },
  "ModifyTableGroupTags": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待修改标签表格组所属集群ID"
      },
      {
        "name": "TableGroupId",
        "desc": "待修改标签表格组ID"
      },
      {
        "name": "ReplaceTags",
        "desc": "待增加或修改的标签列表"
      },
      {
        "name": "DeleteTags",
        "desc": "待删除的标签"
      }
    ],
    "desc": "修改表格组标签"
  },
  "DescribeTableGroupTags": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待查询标签表格组所属集群ID"
      },
      {
        "name": "TableGroupIds",
        "desc": "待查询标签表格组ID列表"
      }
    ],
    "desc": "获取表格组关联的标签列表"
  },
  "DescribeTableGroups": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表格组所属集群ID"
      },
      {
        "name": "TableGroupIds",
        "desc": "表格组ID列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：TableGroupName，TableGroupId"
      },
      {
        "name": "Offset",
        "desc": "查询列表偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询列表返回记录数"
      }
    ],
    "desc": "查询表格组列表"
  },
  "CompareIdlFiles": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待修改表格所在集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待修改表格列表"
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
    "desc": "选中目标表格，上传并校验改表文件，返回是否允许修改表格结构的结果。"
  },
  "DescribeIdlFileInfos": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "文件所属集群ID"
      },
      {
        "name": "TableGroupIds",
        "desc": "文件所属表格组ID"
      },
      {
        "name": "IdlFileIds",
        "desc": "指定文件ID列表"
      },
      {
        "name": "Offset",
        "desc": "查询列表偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询列表返回记录数"
      }
    ],
    "desc": "查询表描述文件详情"
  },
  "DeleteTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待删除表所在集群ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待删除表信息列表"
      }
    ],
    "desc": "删除指定的表,第一次调用此接口代表将表移动至回收站，再次调用代表将此表格从回收站中彻底删除。"
  },
  "ModifyTableMemos": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表所属集群实例ID"
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
        "name": "ClusterId",
        "desc": "待创建表格的集群ID"
      },
      {
        "name": "TableGroupId",
        "desc": "待创建表格的表格组ID"
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
    "desc": "上传并校验创建表格文件，返回校验合法的表格定义"
  },
  "DescribeClusterTags": {
    "params": [
      {
        "name": "ClusterIds",
        "desc": "集群ID列表"
      }
    ],
    "desc": "获取集群关联的标签列表"
  },
  "ModifyTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待修改表格所在集群ID"
      },
      {
        "name": "IdlFiles",
        "desc": "选中的改表IDL文件"
      },
      {
        "name": "SelectedTables",
        "desc": "待改表格列表"
      }
    ],
    "desc": "根据用户选定的表定义IDL文件，批量修改指定的表"
  },
  "DescribeTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "待查询表格所属集群ID"
      },
      {
        "name": "TableGroupIds",
        "desc": "待查询表格所属表格组ID列表"
      },
      {
        "name": "SelectedTables",
        "desc": "待查询表格信息列表"
      },
      {
        "name": "Filters",
        "desc": "过滤条件，本接口支持：TableName，TableInstanceId"
      },
      {
        "name": "Offset",
        "desc": "查询结果偏移量"
      },
      {
        "name": "Limit",
        "desc": "查询结果返回记录数量"
      }
    ],
    "desc": "查询表详情"
  },
  "ClearTables": {
    "params": [
      {
        "name": "ClusterId",
        "desc": "表所属集群实例ID"
      },
      {
        "name": "SelectedTables",
        "desc": "待清理表信息列表"
      }
    ],
    "desc": "根据给定的表信息，清除表数据。"
  }
}