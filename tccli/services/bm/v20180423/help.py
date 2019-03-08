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
  "OfflineDevices": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要退还的物理机ID列表"
      }
    ],
    "desc": "销毁黑石物理机实例：可以销毁物理机列表中的竞价实例，或回收站列表中所有计费模式的实例"
  },
  "DescribeOsInfo": {
    "params": [
      {
        "name": "DeviceClassCode",
        "desc": "设备类型代号。 可以从DescribeDeviceClass查询设备类型列表"
      }
    ],
    "desc": "查询指定机型所支持的操作系统"
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
  "DescribeCustomImageProcess": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像ID"
      }
    ],
    "desc": "查询自定义镜像制作进度"
  },
  "DescribeHardwareSpecification": {
    "params": [],
    "desc": "查询自定义机型部件信息，包括CpuId对应的型号，DiskTypeId对应的磁盘类型"
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
  "DescribeDeviceClass": {
    "params": [],
    "desc": "获取获取设备类型"
  },
  "BuyDevices": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区ID。通过接口[查询地域以及可用区(DescribeRegions)](https://cloud.tencent.com/document/api/386/6634)获取可用区信息"
      },
      {
        "name": "OsTypeId",
        "desc": "部署服务器的操作系统ID。通过接口[查询操作系统信息(DescribeOsInfo)](https://cloud.tencent.com/document/api/386/31964)获取操作系统信息"
      },
      {
        "name": "RaidId",
        "desc": "RAID类型ID。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/7370)获取RAID信息"
      },
      {
        "name": "GoodsCount",
        "desc": "购买数量"
      },
      {
        "name": "VpcId",
        "desc": "购买至私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "购买至子网ID"
      },
      {
        "name": "DeviceClassCode",
        "desc": "购买的机型ID。通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/6636)获取机型信息"
      },
      {
        "name": "TimeUnit",
        "desc": "购买时长单位，取值：M(月) D(天)"
      },
      {
        "name": "TimeSpan",
        "desc": "购买时长"
      },
      {
        "name": "NeedSecurityAgent",
        "desc": "是否安装安全Agent，取值：1(安装) 0(不安装)，默认取值0"
      },
      {
        "name": "NeedMonitorAgent",
        "desc": "是否安装监控Agent，取值：1(安装) 0(不安装)，默认取值0"
      },
      {
        "name": "NeedEMRAgent",
        "desc": "是否安装EMR Agent，取值：1(安装) 0(不安装)，默认取值0"
      },
      {
        "name": "NeedEMRSoftware",
        "desc": "是否安装EMR软件包，取值：1(安装) 0(不安装)，默认取值0"
      },
      {
        "name": "ApplyEip",
        "desc": "是否分配弹性公网IP，取值：1(分配) 0(不分配)，默认取值0"
      },
      {
        "name": "EipPayMode",
        "desc": "弹性公网IP计费模式，取值：Flow(按流量计费) Bandwidth(按带宽计费)，默认取值Flow"
      },
      {
        "name": "EipBandwidth",
        "desc": "弹性公网IP带宽限制，单位Mb"
      },
      {
        "name": "IsZoning",
        "desc": "数据盘是否格式化，取值：1(格式化) 0(不格式化)，默认取值为1"
      },
      {
        "name": "CpmPayMode",
        "desc": "物理机计费模式，取值：1(预付费) 2(后付费)，默认取值为1"
      },
      {
        "name": "ImageId",
        "desc": "自定义镜像ID，取值生效时用自定义镜像部署物理机"
      },
      {
        "name": "Password",
        "desc": "设置Linux root或Windows Administrator的密码"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标志位，取值：1(自动续费) 0(不自动续费)，默认取值0"
      },
      {
        "name": "SysRootSpace",
        "desc": "系统盘根分区大小，单位为G，默认取值10G。通过接口[查询机型RAID方式以及系统盘大小(DescribeDeviceClassPartition)](https://cloud.tencent.com/document/api/386/7370)获取根分区信息"
      },
      {
        "name": "SysSwaporuefiSpace",
        "desc": "系统盘swap分区或/boot/efi分区的大小，单位为G。若是uefi启动的机器，分区为/boot/efi，且此值是默认是2G。 普通机器为swap分区，可以不指定此分区。 机型是否是uefi启动，参见接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/6636)"
      },
      {
        "name": "SysUsrlocalSpace",
        "desc": "/usr/local分区大小，单位为G"
      },
      {
        "name": "SysDataSpace",
        "desc": "/data分区大小，单位为G。如果系统盘还有剩余大小，会分配给/data分区。（特殊情况：如果剩余空间不足10G，并且没有指定/data分区，则剩余空间会分配给Root分区）"
      },
      {
        "name": "HyperThreading",
        "desc": "是否开启超线程，取值：1(开启) 0(关闭)，默认取值1"
      },
      {
        "name": "LanIps",
        "desc": "指定的内网IP列表，不指定时自动分配"
      },
      {
        "name": "Aliases",
        "desc": "设备名称列表"
      },
      {
        "name": "CpuId",
        "desc": "CPU型号ID，自定义机型需要传入，取值：\n<br/><li>1: E5-2620v3 (6核) &#42; 2</li><li>2: E5-2680v4 (14核) &#42; 2</li><li>3: E5-2670v3 (12核) &#42; 2</li><li>4: E5-2620v4 (8核) &#42; 2</li><li>5: 4110 (8核) &#42; 2</li><li>6: 6133 (20核) &#42; 2</li><br/>"
      },
      {
        "name": "ContainRaidCard",
        "desc": "是否有RAID卡，取值：1(有) 0(无)，自定义机型需要传入"
      },
      {
        "name": "MemSize",
        "desc": "内存大小，单位为G，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/10968)返回值"
      },
      {
        "name": "SystemDiskTypeId",
        "desc": "系统盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/10968)返回值"
      },
      {
        "name": "SystemDiskCount",
        "desc": "系统盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/10968)返回值"
      },
      {
        "name": "DataDiskTypeId",
        "desc": "数据盘ID，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/10968)返回值"
      },
      {
        "name": "DataDiskCount",
        "desc": "数据盘数量，自定义机型需要传入。取值参考接口[查询自定义机型部件信息(DescribeHardwareSpecification)](https://cloud.tencent.com/document/api/386/10968)返回值"
      },
      {
        "name": "Tags",
        "desc": "绑定的标签列表"
      }
    ],
    "desc": "购买黑石物理机"
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
  "DescribeHostedDeviceOutBandInfo": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "托管设备的唯一ID数组,数组个数不超过20"
      },
      {
        "name": "Zone",
        "desc": "可用区ID"
      }
    ],
    "desc": "查询托管设备带外信息"
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
  "DeleteCustomImages": {
    "params": [
      {
        "name": "ImageIds",
        "desc": "准备删除的镜像ID列表"
      }
    ],
    "desc": "删除自定义镜像<br>\n正用于部署或重装中的镜像被删除后，镜像文件将保留一段时间，直到部署或重装结束"
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
  "ModifyLanIp": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "物理机ID"
      },
      {
        "name": "VpcId",
        "desc": "指定新VPC"
      },
      {
        "name": "SubnetId",
        "desc": "指定新子网"
      },
      {
        "name": "LanIp",
        "desc": "指定新内网IP"
      },
      {
        "name": "RebootDevice",
        "desc": "是否需要重启机器，取值 1(需要) 0(不需要)，默认取值0"
      }
    ],
    "desc": "修改物理机内网IP（不重装系统）"
  },
  "DescribeOperationResult": {
    "params": [
      {
        "name": "TaskId",
        "desc": "异步任务ID"
      }
    ],
    "desc": "获取异步操作状态的完成状态"
  },
  "ModifyCustomImageAttribute": {
    "params": [
      {
        "name": "ImageId",
        "desc": "镜像ID"
      },
      {
        "name": "ImageName",
        "desc": "设置新的镜像名"
      },
      {
        "name": "ImageDescription",
        "desc": "设置新的镜像描述"
      }
    ],
    "desc": "用于修改自定义镜像名或描述"
  },
  "DescribeDevicePosition": {
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
        "name": "VpcId",
        "desc": "私有网络ID"
      },
      {
        "name": "SubnetId",
        "desc": "子网ID"
      },
      {
        "name": "InstanceIds",
        "desc": "实例ID列表"
      },
      {
        "name": "Alias",
        "desc": "实例别名"
      }
    ],
    "desc": "查询服务器所在的位置，如机架，上联交换机等信息"
  },
  "DescribeDeviceClassPartition": {
    "params": [
      {
        "name": "DeviceClassCode",
        "desc": "设备类型代号。代号通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/17602)查询。标准机型需要传入此参数"
      },
      {
        "name": "InstanceId",
        "desc": "需要查询自定义机型RAID信息时，传入自定义机型实例ID。InstanceId存在时DeviceClassCode失效"
      }
    ],
    "desc": "查询机型支持的RAID方式， 并返回系统盘的分区和逻辑盘的列表"
  },
  "DescribeRegions": {
    "params": [
      {
        "name": "RegionId",
        "desc": "地域整型ID，目前黑石可用地域包括：8-北京，4-上海，1-广州， 19-重庆"
      }
    ],
    "desc": "查询地域以及可用区"
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
  "ReturnDevices": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要退还的物理机ID列表"
      }
    ],
    "desc": "退回物理机至回收站，支持批量退还不同计费模式的物理机（包括预付费、后付费、预付费转后付费）"
  },
  "ModifyDeviceAutoRenewFlag": {
    "params": [
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标志位。0: 不自动续费; 1: 自动续费"
      },
      {
        "name": "InstanceIds",
        "desc": "需要修改的设备ID列表"
      }
    ],
    "desc": "修改物理机服务器自动续费标志"
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
        "desc": "计算单元类型, 如v3.c2.medium，更详细的ComputeType参考[竞价实例产品文档](https://cloud.tencent.com/document/product/386/30256)"
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
  "DescribeDeviceInventory": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区"
      },
      {
        "name": "DeviceClassCode",
        "desc": "设备型号"
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
        "name": "CpuId",
        "desc": "CpuId，自定义机型时需传入"
      },
      {
        "name": "DiskType",
        "desc": "硬盘类型，自定义机型时需传入"
      },
      {
        "name": "DiskSize",
        "desc": "单块硬盘大小，自定义机型时需传入"
      },
      {
        "name": "DiskNum",
        "desc": "硬盘数量，自定义机型时需传入"
      },
      {
        "name": "Mem",
        "desc": "内存总大小，自定义机型时需传入"
      },
      {
        "name": "HaveRaidCard",
        "desc": "是否支持raid，自定义机型时需传入"
      }
    ],
    "desc": "查询设备库存"
  },
  "DescribeDeviceOperationLog": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "设备实例ID"
      },
      {
        "name": "StartTime",
        "desc": "查询开始日期"
      },
      {
        "name": "EndTime",
        "desc": "查询结束日期"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "返回数量"
      }
    ],
    "desc": "查询设备操作日志， 如设备重启，重装，设置密码等操作"
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
        "desc": "机型ID，通过接口[查询设备型号(DescribeDeviceClass)](https://cloud.tencent.com/document/api/386/31968)查询"
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
  "DescribeDeviceHardwareInfo": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "设备 ID 列表"
      }
    ],
    "desc": "查询设备硬件配置信息，如 CPU 型号，内存大小，磁盘大小和数量"
  },
  "DescribeRepairTaskConstant": {
    "params": [],
    "desc": "维修任务配置获取"
  },
  "SetOutBandVpnAuthPassword": {
    "params": [
      {
        "name": "Password",
        "desc": "设置的Vpn认证密码"
      },
      {
        "name": "Operate",
        "desc": "操作字段，取值为：Create（创建）或Update（修改）"
      }
    ],
    "desc": "设置带外VPN认证用户密码"
  },
  "DescribeCustomImages": {
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
        "desc": "排序字段，仅支持CreateTime"
      },
      {
        "name": "Order",
        "desc": "排序方式 0:递增(默认) 1:递减"
      },
      {
        "name": "ImageId",
        "desc": "按ImageId查找指定镜像信息，ImageId字段存在时其他字段失效"
      },
      {
        "name": "SearchKey",
        "desc": "模糊查询过滤，可以查询镜像ID或镜像名"
      },
      {
        "name": "ImageStatus",
        "desc": "<ul>\n镜像状态过滤列表，有效取值为：\n<li>1：制作中</li>\n<li>2：制作失败</li>\n<li>3：正常</li>\n<li>4：删除中</li>\n</ul>"
      }
    ],
    "desc": "查看自定义镜像列表"
  },
  "RecoverDevices": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要恢复的物理机ID列表"
      }
    ],
    "desc": "恢复回收站中的物理机（仅限后付费的物理机）"
  },
  "DescribeDevicePartition": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "物理机ID"
      }
    ],
    "desc": "获取物理机的分区格式"
  },
  "ShutdownDevices": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "需要关闭的设备ID列表"
      }
    ],
    "desc": "关闭服务器"
  },
  "ModifyDeviceAliases": {
    "params": [
      {
        "name": "DeviceAliases",
        "desc": "需要改名的设备与别名列表"
      }
    ],
    "desc": "修改服务器名称"
  },
  "CreateCustomImage": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "用于制作镜像的物理机ID"
      },
      {
        "name": "ImageName",
        "desc": "镜像别名"
      },
      {
        "name": "ImageDescription",
        "desc": "镜像描述"
      }
    ],
    "desc": "创建自定义镜像<br>\n每个AppId在每个可用区最多保留20个自定义镜像"
  }
}