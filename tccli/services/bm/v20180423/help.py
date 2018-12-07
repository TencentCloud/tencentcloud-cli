# -*- coding: utf-8 -*-
DESC = "bm-2018-04-23"
INFO = {
  "DescribeUserCmds": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "数量限制"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，支持： OsType,CreateTime,ModifyTime"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值: 1倒序，0顺序；默认倒序"
      },
      {
        "name": "SearchKey",
        "desc": "关键字搜索，可搜索ID或别名，支持模糊搜索"
      },
      {
        "name": "CmdId",
        "desc": "查询的脚本ID"
      }
    ],
    "desc": "获取自定义脚本信息列表"
  },
  "ModifyPsaRegulation": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "PsaName",
        "desc": "预授权规则别名"
      },
      {
        "name": "RepairLimit",
        "desc": "维修中的实例上限"
      },
      {
        "name": "PsaDescription",
        "desc": "预授权规则备注"
      },
      {
        "name": "TaskTypeIds",
        "desc": "预授权规则关联故障类型ID列表"
      }
    ],
    "desc": "允许修改规则信息及关联故障类型"
  },
  "DescribePsaRegulations": {
    "params": [
      {
        "name": "Limit",
        "desc": "数量限制"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "PsaIds",
        "desc": "规则ID过滤，支持模糊查询"
      },
      {
        "name": "PsaNames",
        "desc": "规则别名过滤，支持模糊查询"
      },
      {
        "name": "Tags",
        "desc": "标签过滤"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，取值支持：CreateTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      }
    ],
    "desc": "获取预授权规则列表"
  },
  "RunUserCmd": {
    "params": [
      {
        "name": "CmdId",
        "desc": "自定义脚本ID"
      },
      {
        "name": "UserName",
        "desc": "执行脚本机器的用户名"
      },
      {
        "name": "Password",
        "desc": "执行脚本机器的用户名的密码"
      },
      {
        "name": "InstanceIds",
        "desc": "执行脚本的服务器实例"
      },
      {
        "name": "CmdParam",
        "desc": "执行脚本的参数，必须经过base64编码"
      }
    ],
    "desc": "运行自定义脚本"
  },
  "DescribeUserCmdTasks": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "数量限制"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，支持： RunBeginTime,RunEndTime,InstanceCount,SuccessCount,FailureCount"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值: 1倒序，0顺序；默认倒序"
      }
    ],
    "desc": "获取自定义脚本任务列表"
  },
  "CreatePsaRegulation": {
    "params": [
      {
        "name": "PsaName",
        "desc": "规则别名"
      },
      {
        "name": "TaskTypeIds",
        "desc": "关联的故障类型ID列表"
      },
      {
        "name": "RepairLimit",
        "desc": "维修实例上限，默认为5"
      },
      {
        "name": "PsaDescription",
        "desc": "规则备注"
      }
    ],
    "desc": "创建预授权规则"
  },
  "ModifyUserCmd": {
    "params": [
      {
        "name": "CmdId",
        "desc": "待修改的脚本ID"
      },
      {
        "name": "Alias",
        "desc": "待修改的脚本名称"
      },
      {
        "name": "OsType",
        "desc": "脚本适用的操作系统类型"
      },
      {
        "name": "Content",
        "desc": "待修改的脚本内容，必须经过base64编码"
      }
    ],
    "desc": "修改自定义脚本"
  },
  "DeleteUserCmds": {
    "params": [
      {
        "name": "CmdIds",
        "desc": "需要删除的脚本ID"
      }
    ],
    "desc": "删除自定义脚本"
  },
  "BindPsaTag": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "TagKey",
        "desc": "需要绑定的标签key"
      },
      {
        "name": "TagValue",
        "desc": "需要绑定的标签value"
      }
    ],
    "desc": "为预授权规则绑定标签"
  },
  "DeletePsaRegulation": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      }
    ],
    "desc": "删除预授权规则"
  },
  "CreateUserCmd": {
    "params": [
      {
        "name": "Alias",
        "desc": "用户自定义脚本的名称"
      },
      {
        "name": "OsType",
        "desc": "命令适用的操作系统类型，取值linux或xserver"
      },
      {
        "name": "Content",
        "desc": "脚本内容，必须经过base64编码"
      }
    ],
    "desc": "创建自定义脚本"
  },
  "DescribeTaskInfo": {
    "params": [
      {
        "name": "Offset",
        "desc": "开始位置"
      },
      {
        "name": "Limit",
        "desc": "数据条数"
      },
      {
        "name": "StartDate",
        "desc": "时间过滤下限"
      },
      {
        "name": "EndDate",
        "desc": "时间过滤上限"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态ID过滤"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，目前支持：CreateTime，AuthTime，EndTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      },
      {
        "name": "TaskIds",
        "desc": "任务ID过滤"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID过滤"
      },
      {
        "name": "Aliases",
        "desc": "实例别名过滤"
      },
      {
        "name": "TaskTypeIds",
        "desc": "故障类型ID过滤"
      }
    ],
    "desc": "获取用户维修任务列表及详细信息<br>\n<br>\nTaskStatus（任务状态ID）与状态中文名的对应关系如下：<br>\n1：未授权<br>\n2：处理中<br>\n3：待确认<br>\n4：未授权-暂不处理<br>\n5：已恢复<br>\n6：待确认-未恢复<br>"
  },
  "RebootDevices": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要重启的设备ID列表"
      }
    ],
    "desc": "重启机器"
  },
  "DescribeUserCmdTaskInfo": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "数量限制"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，支持： RunBeginTime,RunEndTime,Status"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值: 1倒序，0顺序；默认倒序"
      },
      {
        "name": "SearchKey",
        "desc": "关键字搜索，可搜索ID或别名，支持模糊搜索"
      }
    ],
    "desc": "获取自定义脚本任务详细信息"
  },
  "DescribeDevicePriceInfo": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要查询的实例列表"
      },
      {
        "name": "TimeUnit",
        "desc": "购买时长单位，当前只支持取值为m"
      },
      {
        "name": "TimeSpan",
        "desc": "购买时长"
      }
    ],
    "desc": "查询服务器价格信息，支持设备的批量查找，支持标准机型和弹性机型的混合查找"
  },
  "DescribeTaskOperationLog": {
    "params": [
      {
        "name": "TaskId",
        "desc": "维修任务ID"
      },
      {
        "name": "OrderField",
        "desc": "排序字段，目前支持：OperationTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      }
    ],
    "desc": "获取维修任务操作日志"
  },
  "ModifyPayModePre2Post": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要修改的设备ID列表"
      }
    ],
    "desc": "将设备的预付费模式修改为后付费计费模式，支持批量转换。（前提是客户要加入黑石物理机后付费计费的白名单，申请黑石物理机后付费可以联系腾讯云客服）"
  },
  "UnbindPsaTag": {
    "params": [
      {
        "name": "PsaId",
        "desc": "预授权规则ID"
      },
      {
        "name": "TagKey",
        "desc": "需要解绑的标签key"
      },
      {
        "name": "TagValue",
        "desc": "需要解绑的标签value"
      }
    ],
    "desc": "解除标签与预授权规则的绑定"
  },
  "CreateSpotDevice": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区名称。如ap-guangzhou-bls-1, 通过DescribeRegions获取"
      },
      {
        "name": "ComputeType",
        "desc": "计算单元类型"
      },
      {
        "name": "OsTypeId",
        "desc": "操作系统类型ID"
      },
      {
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "GoodsNum",
        "desc": "购买的计算单元个数"
      },
      {
        "name": "SpotStrategy",
        "desc": "出价策略。可取值为SpotWithPriceLimit和SpotAsPriceGo。SpotWithPriceLimit，用户设置价格上限，需要传SpotPriceLimit参数， 如果市场价高于用户的指定价格，则购买不成功;  SpotAsPriceGo 是随市场价的策略。"
      },
      {
        "name": "SpotPriceLimit",
        "desc": "用户设置的价格。当为SpotWithPriceLimit竞价策略时有效"
      },
      {
        "name": "Passwd",
        "desc": "设置竞价实例密码。可选参数，没有指定会生成随机密码"
      }
    ],
    "desc": "创建黑石竞价实例"
  },
  "ResetDevicePassword": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要重置密码的服务器ID列表"
      },
      {
        "name": "Password",
        "desc": "新密码"
      }
    ],
    "desc": "重置服务器密码"
  },
  "RepairTaskControl": {
    "params": [
      {
        "name": "TaskId",
        "desc": "维修任务ID"
      },
      {
        "name": "Operate",
        "desc": "操作"
      }
    ],
    "desc": "此接口用于操作维修任务<br>\n入参TaskId为维修任务ID<br>\n入参Operate表示对维修任务的操作，支持如下取值：<br>\nAuthorizeRepair（授权维修）<br>\nIgnore（暂不提醒）<br>\nConfirmRecovered（维修完成后，确认故障恢复）<br>\nConfirmUnRecovered（维修完成后，确认故障未恢复）<br>\n<br>\n操作约束（当前任务状态(TaskStatus)->对应可执行的操作）：<br>\n未授权(1)->授权维修；暂不处理<br>\n暂不处理(4)->授权维修<br>\n待确认(3)->确认故障恢复；确认故障未恢复<br>\n未恢复(6)->确认故障恢复<br>\n<br>\n对于Ping不可达故障的任务，还允许：<br>\n未授权->确认故障恢复<br>\n暂不处理->确认故障恢复<br>\n<br>\n处理中与已恢复状态的任务不允许进行操作。<br>\n<br>\n详细信息请访问：https://cloud.tencent.com/document/product/386/18190"
  },
  "DescribeDevices": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      },
      {
        "name": "DeviceClassCode",
        "desc": "机型ID，通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/17602)查询"
      },
      {
        "name": "InstanceIds",
        "desc": "设备ID数组"
      },
      {
        "name": "WanIps",
        "desc": "外网IP数组"
      },
      {
        "name": "LanIps",
        "desc": "内网IP数组"
      },
      {
        "name": "Alias",
        "desc": "设备名称"
      },
      {
        "name": "VagueIp",
        "desc": "模糊IP查询"
      },
      {
        "name": "DeadlineStartTime",
        "desc": "设备到期时间查询的起始时间"
      },
      {
        "name": "DeadlineEndTime",
        "desc": "设备到期时间查询的结束时间"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标志 0:不自动续费，1:自动续费"
      },
      {
        "name": "VpcId",
        "desc": "私有网络唯一ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网唯一ID"
      },
      {
        "name": "Tags",
        "desc": "标签列表"
      },
      {
        "name": "DeviceType",
        "desc": "设备类型，取值有: compute(计算型), standard(标准型), storage(存储型) 等"
      },
      {
        "name": "IsLuckyDevice",
        "desc": "竞价实例机器的过滤。如果未指定此参数，则不做过滤。0: 查询非竞价实例的机器; 1: 查询竞价实例的机器。"
      },
      {
        "name": "OrderField",
        "desc": "排序字段"
      },
      {
        "name": "Order",
        "desc": "排序方式，取值：0:增序(默认)，1:降序"
      }
    ],
    "desc": "查询物理服务器，可以按照实例，业务IP等过滤"
  },
  "DescribeRepairTaskConstant": {
    "params": [],
    "desc": "维修任务配置获取"
  },
  "ModifyDeviceAliases": {
    "params": [
      {
        "name": "DeviceAliases",
        "desc": "需要改名的设备与别名列表"
      }
    ],
    "desc": "修改服务器名称"
  }
}