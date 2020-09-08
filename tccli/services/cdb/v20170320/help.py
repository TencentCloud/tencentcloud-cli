# -*- coding: utf-8 -*-
DESC = "cdb-2017-03-20"
INFO = {
  "DescribeDBInstanceGTID": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了 GTID，不支持版本为 5.5 以及以下的实例。"
  },
  "CreateRoInstanceIp": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "只读实例ID，格式如：cdbro-3i70uj0k，与云数据库控制台页面中显示的只读实例ID相同。"
      },
      {
        "name": "UniqSubnetId",
        "desc": "子网描述符，例如：subnet-1typ0s7d。"
      },
      {
        "name": "UniqVpcId",
        "desc": "vpc描述符，例如：vpc-xxx,如果传了该字段则UniqSubnetId必传"
      }
    ],
    "desc": "本接口(CreateRoInstanceIp)用于创建云数据库只读实例的独立VIP。"
  },
  "CreateAuditPolicy": {
    "params": [
      {
        "name": "Name",
        "desc": "审计策略名称。"
      },
      {
        "name": "RuleId",
        "desc": "审计规则 ID。"
      },
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "LogExpireDay",
        "desc": "审计日志保存时长。支持值包括：\n30 - 一个月；\n180 - 六个月；\n365 - 一年；\n1095 - 三年；\n1825 - 五年；\n实例首次开通审计策略时，可传该值，用于设置存储日志保存天数，默认为 30 天。若实例已存在审计策略，则此参数无效，可使用 更改审计服务配置 接口修改日志存储时长。"
      }
    ],
    "desc": "本接口(CreateAuditPolicy)用于创建云数据库实例的审计策略，即将审计规则绑定到具体的云数据库实例上。"
  },
  "DescribeDataBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "需要查询的云数据库产品类型，目前仅支持 \"mysql\"。"
      }
    ],
    "desc": "本接口(DescribeDataBackupOverview)用于查询用户在当前地域总的数据备份概览。"
  },
  "BalanceRoGroupLoad": {
    "params": [
      {
        "name": "RoGroupId",
        "desc": "RO 组的 ID，格式如：cdbrg-c1nl9rpv。"
      }
    ],
    "desc": "本接口(BalanceRoGroupLoad)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。"
  },
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(IsolateDBInstance)用于隔离云数据库实例，隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。"
  },
  "RestartDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(RestartDBInstances)用于重启云数据库实例。\n\n注意：\n1、本接口只支持主实例进行重启操作；\n2、实例状态必须为正常，并且没有其他异步任务在执行中。"
  },
  "ModifyInstanceTag": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      },
      {
        "name": "ReplaceTags",
        "desc": "要增加或修改的标签。"
      },
      {
        "name": "DeleteTags",
        "desc": "要删除的标签。"
      }
    ],
    "desc": "本接口(ModifyInstanceTag)用于对实例标签进行添加、修改或者删除。"
  },
  "DescribeTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeTimeWindow)用于查询云数据库实例的维护时间窗口。"
  },
  "DescribeBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "需要查询的云数据库产品类型，目前仅支持 \"mysql\"。"
      }
    ],
    "desc": "本接口(DescribeBackupOverview)用于查询用户的备份概览。返回用户当前备份总个数、备份总的占用容量、赠送的免费容量、计费容量（容量单位为字节）。"
  },
  "ModifyDBInstanceName": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。"
  },
  "OfflineIsolatedInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(OfflineIsolatedInstances)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态，即通过 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询到 Status 值为 5 的实例。\n\n该接口为异步操作，部分资源的回收可能存在延迟。您可以通过使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口，指定实例 InstanceId 和状态 Status 为 [5,6,7] 进行查询，若返回实例为空，则实例资源已全部释放。\n\n注意，实例下线后，相关资源和数据将无法找回，请谨慎操作。"
  },
  "CreateAuditLogFile": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：\"2017-07-12 10:29:20\"。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，格式为：\"2017-07-12 10:29:20\"。"
      },
      {
        "name": "Order",
        "desc": "排序方式。支持值包括：\"ASC\" - 升序，\"DESC\" - 降序。"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段。支持值包括：\n\"timestamp\" - 时间戳；\n\"affectRows\" - 影响行数；\n\"execTime\" - 执行时间。"
      },
      {
        "name": "Filter",
        "desc": "过滤条件。可按设置的过滤条件过滤日志。"
      }
    ],
    "desc": "本接口(CreateAuditLogFile)用于创建云数据库实例的审计日志文件。"
  },
  "OpenDBInstanceGTID": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(OpenDBInstanceGTID)用于开启云数据库实例的 GTID，只支持版本为 5.6 以及以上的实例。"
  },
  "DescribeRollbackTaskDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。"
      },
      {
        "name": "AsyncRequestId",
        "desc": "异步任务 ID。"
      },
      {
        "name": "Limit",
        "desc": "分页参数，每次请求返回的记录数。默认值为 20，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。默认为 0。"
      }
    ],
    "desc": "本接口(DescribeRollbackTaskDetail)用于查询云数据库实例回档任务详情。"
  },
  "ModifyDBInstanceSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "SecurityGroupIds",
        "desc": "要修改的安全组 ID 列表，一个或者多个安全组 ID 组成的数组。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "AsyncRequestId",
        "desc": "异步任务请求 ID，执行云数据库相关操作返回的 AsyncRequestId。"
      },
      {
        "name": "TaskTypes",
        "desc": "任务类型，不传值则查询所有任务类型，支持的值包括：\n1 - 数据库回档；\n2 - SQL操作；\n3 - 数据导入；\n5 - 参数设置；\n6 - 初始化云数据库实例；\n7 - 重启云数据库实例；\n8 - 开启云数据库实例GTID；\n9 - 只读实例升级；\n10 - 数据库批量回档；\n11 - 主实例升级；\n12 - 删除云数据库库表；\n13 - 灾备实例提升为主。"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态，不传值则查询所有任务状态，支持的值包括：\n-1 - 未定义；\n0 - 初始化；\n1 - 运行中；\n2 - 执行成功；\n3 - 执行失败；\n4 - 已终止；\n5 - 已删除；\n6 - 已暂停。"
      },
      {
        "name": "StartTimeBegin",
        "desc": "第一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。"
      },
      {
        "name": "StartTimeEnd",
        "desc": "最后一个任务的开始时间，用于范围查询，时间格式如：2017-12-31 10:40:01。"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeTasks)用于查询云数据库实例任务列表。"
  },
  "DescribeBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeBackupConfig)用于查询数据库备份配置信息。"
  },
  "CloseWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。"
  },
  "DescribeDefaultParams": {
    "params": [
      {
        "name": "EngineVersion",
        "desc": "mysql版本，目前支持 [\"5.1\", \"5.5\", \"5.6\", \"5.7\"]。"
      }
    ],
    "desc": "该接口（DescribeDefaultParams）用于查询默认的可设置参数列表。"
  },
  "DescribeAuditPolicies": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "PolicyId",
        "desc": "审计策略 ID。"
      },
      {
        "name": "PolicyName",
        "desc": "审计策略名称。支持按审计策略名称进行模糊匹配查询。"
      },
      {
        "name": "Limit",
        "desc": "分页大小参数。默认值为 20，最小值为 1，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "RuleId",
        "desc": "审计规则 ID。可使用该审计规则 ID 查询到其关联的审计策略。\n注意，参数 RuleId，InstanceId，PolicyId，PolicyName 必须至少传一个。"
      }
    ],
    "desc": "本接口(DescribeAuditPolicies)用于查询云数据库实例的审计策略。"
  },
  "DescribeTagsOfInstanceIds": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例列表。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页大小。"
      }
    ],
    "desc": "本接口(DescribeTagsOfInstanceIds)用于获取云数据库实例的标签信息。"
  },
  "DescribeDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求数量，默认值为20，最小值为1，最大值为100。"
      },
      {
        "name": "DatabaseRegexp",
        "desc": "匹配数据库库名的正则表达式。"
      }
    ],
    "desc": "本接口(DescribeDatabases)用于查询云数据库实例的数据库信息。"
  },
  "DescribeErrorLogData": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间戳。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间戳。"
      },
      {
        "name": "KeyWords",
        "desc": "要匹配的关键字列表，最多支持15个关键字。"
      },
      {
        "name": "Limit",
        "desc": "分页的返回数量，最大为400。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "根据检索条件查询实例错误日志详情。只能查询一个月之内的错误日志。"
  },
  "DisassociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组 ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表，一个或者多个实例 ID 组成的数组。"
      }
    ],
    "desc": "本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。"
  },
  "DescribeTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Database",
        "desc": "数据库的名称。"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最大值为2000。"
      },
      {
        "name": "TableRegexp",
        "desc": "匹配数据库表名的正则表达式，规则同 MySQL 官网"
      }
    ],
    "desc": "本接口(DescribeTables)用于查询云数据库实例的数据库表信息。"
  },
  "DescribeAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "User",
        "desc": "数据库的账号名称。"
      },
      {
        "name": "Host",
        "desc": "数据库的账号域名。"
      }
    ],
    "desc": "本接口(DescribeAccountPrivileges)用于查询云数据库账户支持的权限信息。"
  },
  "ReleaseIsolatedDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 数组，单个实例 ID 格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口（ReleaseIsolatedDBInstances）用于恢复已隔离云数据库实例。"
  },
  "ModifyAuditConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      },
      {
        "name": "LogExpireDay",
        "desc": "审计日志保存时长。支持值包括：\n30 - 一个月；\n180 - 六个月；\n365 - 一年；\n1095 - 三年；\n1825 - 五年；"
      },
      {
        "name": "CloseAudit",
        "desc": "是否关闭审计服务。可选值：true - 关闭审计服务；false - 不关闭审计服务。默认值为 false。\n当关闭审计服务时，会删除用户的审计日志和文件，并删除该实例的所有审计策略。"
      }
    ],
    "desc": "本接口(ModifyAuditConfig)用于修改云数据库审计策略的服务配置，包括审计日志保存时长等。"
  },
  "ModifyTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "TimeRanges",
        "desc": "修改后的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起止时间按半个小时对齐；最短半个小时，最长三个小时；最多设置两个时间段；起止时间范围为：[00:00, 24:00]。"
      },
      {
        "name": "Weekdays",
        "desc": "指定修改哪一天的客户时间段，可能的取值为：monday，tuesday，wednesday，thursday，friday，saturday，sunday。如果不指定该值或者为空，则默认一周七天都修改。"
      }
    ],
    "desc": "本接口(ModifyTimeWindow)用于更新云数据库实例的维护时间窗口。"
  },
  "DeleteDeployGroups": {
    "params": [
      {
        "name": "DeployGroupIds",
        "desc": "要删除的置放群组 ID 列表。"
      }
    ],
    "desc": "根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）"
  },
  "SwitchForUpgrade": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程。"
  },
  "DeleteParamTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "参数模板ID。"
      }
    ],
    "desc": "该接口（DeleteParamTemplate）用于删除参数模板。"
  },
  "DescribeBackups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值为20，最小值为1，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeBackups)用于查询云数据库实例的备份数据。"
  },
  "CreateParamTemplate": {
    "params": [
      {
        "name": "Name",
        "desc": "参数模板名称。"
      },
      {
        "name": "Description",
        "desc": "参数模板描述。"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL 版本号。"
      },
      {
        "name": "TemplateId",
        "desc": "源参数模板 ID。"
      },
      {
        "name": "ParamList",
        "desc": "参数列表。"
      }
    ],
    "desc": "该接口（CreateParamTemplate）用于创建参数模板。"
  },
  "CreateDBInstanceHour": {
    "params": [
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为 1，最小值 1，最大值为 100。"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL 版本，值包括：5.5、5.6 和 5.7，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。"
      },
      {
        "name": "UniqSubnetId",
        "desc": "私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/document/api/215/15784)。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID，不填为默认项目。请使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口获取项目 ID。"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。"
      },
      {
        "name": "MasterInstanceId",
        "desc": "实例 ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例 ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。"
      },
      {
        "name": "MasterRegion",
        "desc": "主实例的可用区信息，购买灾备实例时必填。"
      },
      {
        "name": "Port",
        "desc": "自定义端口，端口支持范围：[ 1024-65535 ] 。"
      },
      {
        "name": "Password",
        "desc": "设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "ParamList",
        "desc": "参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "DeployMode",
        "desc": "多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "SlaveZone",
        "desc": "备库 1 的可用区信息，默认为 Zone 的值，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "BackupZone",
        "desc": "备库 2 的可用区信息，默认为空，购买强同步主实例时可指定该参数，购买其他类型实例时指定该参数无意义。"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。"
      },
      {
        "name": "RoGroup",
        "desc": "只读实例信息。购买只读实例时，该参数必传。"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "购买按量计费实例该字段无意义。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。"
      },
      {
        "name": "ResourceTags",
        "desc": "实例标签信息。"
      },
      {
        "name": "DeployGroupId",
        "desc": "置放群组 ID。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在当天内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      },
      {
        "name": "DeviceType",
        "desc": "实例类型。支持值包括： \"HA\" - 高可用版实例， \"BASIC\" - 基础版实例。 不指定则默认为高可用版。"
      }
    ],
    "desc": "本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。\n\n该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为 1，且 TaskStatus 为 0，表示实例已经发货成功。\n\n1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；\n2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；\n3. 支持创建 MySQL 5.5、MySQL 5.6 和 MySQL 5.7 版本；\n4. 支持创建主实例、灾备实例和只读实例；\n5. 当入参指定 Port，ParamList 或 Password 时，该实例会进行初始化操作；"
  },
  "AddTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Monday",
        "desc": "星期一的可维护时间段，其中每一个时间段的格式形如：10:00-12:00；起始时间按半个小时对齐；最短半个小时，最长三个小时；最多设置两个时间段；下同。"
      },
      {
        "name": "Tuesday",
        "desc": "星期二的可维护时间窗口。"
      },
      {
        "name": "Wednesday",
        "desc": "星期三的可维护时间窗口。"
      },
      {
        "name": "Thursday",
        "desc": "星期四的可维护时间窗口。"
      },
      {
        "name": "Friday",
        "desc": "星期五的可维护时间窗口。"
      },
      {
        "name": "Saturday",
        "desc": "星期六的可维护时间窗口。"
      },
      {
        "name": "Sunday",
        "desc": "星期日的可维护时间窗口。"
      }
    ],
    "desc": "本接口(AddTimeWindow)用于添加云数据库实例的维护时间窗口，以指定实例在哪些时间段可以自动执行切换访问操作。"
  },
  "CreateBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "BackupMethod",
        "desc": "目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备。"
      },
      {
        "name": "BackupDBTableList",
        "desc": "需要备份的库表信息，如果不设置该参数，则默认整实例备份。在 BackupMethod=logical 逻辑备份中才可设置该参数。指定的库表必须存在，否则可能导致备份失败。\n例：如果需要备份 db1 库的 tb1、tb2 表 和 db2 库。则该参数设置为 [{\"Db\": \"db1\", \"Table\": \"tb1\"}, {\"Db\": \"db1\", \"Table\": \"tb2\"}, {\"Db\": \"db2\"} ]。"
      }
    ],
    "desc": "本接口(CreateBackup)用于创建数据库备份。"
  },
  "ModifyDBInstanceVipVport": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "DstIp",
        "desc": "目标 IP。该参数和 DstPort 参数，两者必传一个。"
      },
      {
        "name": "DstPort",
        "desc": "目标端口，支持范围为：[1024-65535]。该参数和 DstIp 参数，两者必传一个。"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络统一 ID。"
      },
      {
        "name": "UniqSubnetId",
        "desc": "子网统一 ID。"
      },
      {
        "name": "ReleaseDuration",
        "desc": "进行基础网络转 VPC 网络和 VPC 网络下的子网变更时，原网络中旧IP的回收时间，单位为小时，取值范围为0-168，默认值为24小时。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceVipVport)用于修改云数据库实例的IP和端口号，也可进行基础网络转 VPC 网络和 VPC 网络下的子网变更。"
  },
  "DescribeDBInstanceConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceConfig)用于云数据库实例的配置信息，包括同步模式，部署模式等。"
  },
  "DescribeBackupTables": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：2017-07-12 10:29:20。"
      },
      {
        "name": "DatabaseName",
        "desc": "指定的数据库名。"
      },
      {
        "name": "SearchTable",
        "desc": "要查询的数据表名前缀。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，最小值为1，最大值为2000。"
      }
    ],
    "desc": "本接口(DescribeBackupTables)用于查询指定的数据库的备份数据表名 (已废弃)。\n旧版本支持全量备份后，用户如果分库表下载逻辑备份文件，需要用到此接口。\n新版本支持(CreateBackup)创建逻辑备份的时候，直接发起指定库表备份，用户直接下载该备份文件即可。"
  },
  "DeleteAuditPolicy": {
    "params": [
      {
        "name": "PolicyId",
        "desc": "审计策略 ID。"
      },
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      }
    ],
    "desc": "本接口(DeleteAuditPolicy)用于删除用户的审计策略。"
  },
  "DescribeProjectSecurityGroups": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目ID。"
      }
    ],
    "desc": "本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。"
  },
  "DescribeSlowLogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值为20，最小值为1，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。"
  },
  "InquiryPriceUpgradeInstances": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "Memory",
        "desc": "升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。"
      },
      {
        "name": "Volume",
        "desc": "升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。"
      },
      {
        "name": "Cpu",
        "desc": "升级后的核心数目，单位：核，为保证传入 CPU 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的核心数目，当未指定该值时，将按照 Memory 大小补全一个默认值。"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。"
      }
    ],
    "desc": "本接口(InquiryPriceUpgradeInstances)用于查询云数据库实例升级的价格，支持查询按量计费或者包年包月实例的升级价格，实例类型支持主实例、灾备实例和只读实例。"
  },
  "CreateDBInstance": {
    "params": [
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的内存规格。"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的硬盘范围。"
      },
      {
        "name": "Period",
        "desc": "实例时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为1, 最小值1，最大值为100。"
      },
      {
        "name": "Zone",
        "desc": "可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的可用区。"
      },
      {
        "name": "UniqVpcId",
        "desc": "私有网络 ID，如果不传则默认选择基础网络，请使用 [查询私有网络列表](/document/api/215/15778) 。"
      },
      {
        "name": "UniqSubnetId",
        "desc": "私有网络下的子网 ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用 [查询子网列表](/document/api/215/15784)。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID，不填为默认项目。请使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口获取项目 ID。购买只读实例和灾备实例时，项目 ID 默认和主实例保持一致。"
      },
      {
        "name": "Port",
        "desc": "自定义端口，端口支持范围：[ 1024-65535 ]。"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。"
      },
      {
        "name": "MasterInstanceId",
        "desc": "实例 ID，购买只读实例时必填，该字段表示只读实例的主实例ID，请使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询云数据库实例 ID。"
      },
      {
        "name": "EngineVersion",
        "desc": "MySQL 版本，值包括：5.5、5.6 和 5.7，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口获取可创建的实例版本。"
      },
      {
        "name": "Password",
        "desc": "设置 root 帐号密码，密码规则：8 - 64 个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。"
      },
      {
        "name": "DeployMode",
        "desc": "多可用区域，默认为 0，支持值包括：0 - 表示单可用区，1 - 表示多可用区。"
      },
      {
        "name": "SlaveZone",
        "desc": "备库 1 的可用区信息，默认为 Zone 的值。"
      },
      {
        "name": "ParamList",
        "desc": "参数列表，参数格式如 ParamList.0.Name=auto_increment&ParamList.0.Value=1。可通过 [查询默认的可设置参数列表](https://cloud.tencent.com/document/api/236/32662) 查询支持设置的参数。"
      },
      {
        "name": "BackupZone",
        "desc": "备库 2 的可用区信息，默认为空，购买强同步主实例时可指定该参数，购买其他类型实例时指定该参数无意义。"
      },
      {
        "name": "AutoRenewFlag",
        "desc": "自动续费标记，可选值为：0 - 不自动续费；1 - 自动续费。"
      },
      {
        "name": "MasterRegion",
        "desc": "主实例地域信息，购买灾备实例时，该字段必填。"
      },
      {
        "name": "SecurityGroup",
        "desc": "安全组参数，可使用 [查询项目安全组信息](https://cloud.tencent.com/document/api/236/15850) 接口查询某个项目的安全组详情。"
      },
      {
        "name": "RoGroup",
        "desc": "只读实例参数。购买只读实例时，该参数必传。"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称。"
      },
      {
        "name": "ResourceTags",
        "desc": "实例标签信息。"
      },
      {
        "name": "DeployGroupId",
        "desc": "置放群组 ID。"
      },
      {
        "name": "ClientToken",
        "desc": "用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间在当天内唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。"
      },
      {
        "name": "DeviceType",
        "desc": "实例类型。支持值包括： \"HA\" - 高可用版实例， \"BASIC\" - 基础版实例。 不指定则默认为高可用版。"
      }
    ],
    "desc": "本接口(CreateDBInstance)用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。\n\n该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为1，且 TaskStatus 为0，表示实例已经发货成功。\n\n1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；\n2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；\n3. 支持创建 MySQL 5.5 、 MySQL 5.6 、 MySQL 5.7 版本；\n4. 支持创建主实例、只读实例、灾备实例；\n5. 当入参指定 Port，ParamList 或 Password 时，该实例会进行初始化操作；"
  },
  "ModifyParamTemplate": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "模板 ID。"
      },
      {
        "name": "Name",
        "desc": "模板名称。"
      },
      {
        "name": "Description",
        "desc": "模板描述。"
      },
      {
        "name": "ParamList",
        "desc": "参数列表。"
      }
    ],
    "desc": "该接口（ModifyParamTemplate）用于修改参数模板。"
  },
  "DescribeInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "该接口（DescribeInstanceParams）用于查询实例的参数列表。"
  },
  "DescribeDeployGroupList": {
    "params": [
      {
        "name": "DeployGroupId",
        "desc": "置放群组 ID。"
      },
      {
        "name": "DeployGroupName",
        "desc": "置放群组名称。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为20，最大值为100。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      }
    ],
    "desc": "本接口(DescribeDeployGroupList)用于查询用户的置放群组列表，可以指定置放群组 ID 或置放群组名称。"
  },
  "StopDBImportJob": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "异步任务的请求 ID。"
      }
    ],
    "desc": "本接口(StopDBImportJob)用于终止数据导入任务。"
  },
  "CreateAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Accounts",
        "desc": "云数据库账号。"
      },
      {
        "name": "Password",
        "desc": "新账户的密码。"
      },
      {
        "name": "Description",
        "desc": "备注信息。"
      }
    ],
    "desc": "本接口(CreateAccounts)用于创建云数据库的账户，需要指定新的账户名和域名，以及所对应的密码，同时可以设置账号的备注信息。"
  },
  "UpgradeDBInstanceEngineVersion": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "EngineVersion",
        "desc": "主实例数据库引擎版本，支持值包括：5.6 和 5.7。"
      },
      {
        "name": "WaitSwitch",
        "desc": "切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。"
      },
      {
        "name": "UpgradeSubversion",
        "desc": "是否是内核子版本升级，支持的值：1 - 升级内核子版本；0 - 升级数据库引擎版本。"
      }
    ],
    "desc": "本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。"
  },
  "DescribeAuditLogFiles": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Limit",
        "desc": "分页大小参数。默认值为 20，最小值为 1，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "FileName",
        "desc": "审计日志文件名。"
      }
    ],
    "desc": "本接口(DescribeAuditLogFiles)用于查询云数据库实例的审计日志文件。"
  },
  "DescribeInstanceParamRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页大小。"
      }
    ],
    "desc": "该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。"
  },
  "DescribeBackupSummaries": {
    "params": [
      {
        "name": "Product",
        "desc": "需要查询的云数据库产品类型，目前仅支持 \"mysql\"。"
      },
      {
        "name": "Offset",
        "desc": "分页查询数据的偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页查询数据的条目限制，默认值为20。"
      },
      {
        "name": "OrderBy",
        "desc": "指定按某一项排序，可选值包括： BackupVolume: 备份容量， DataBackupVolume: 数据备份容量， BinlogBackupVolume: 日志备份容量， AutoBackupVolume: 自动备份容量， ManualBackupVolume: 手动备份容量。"
      },
      {
        "name": "OrderDirection",
        "desc": "指定排序方向，可选值包括： ASC: 正序， DESC: 逆序。"
      }
    ],
    "desc": "本接口(DescribeBackupSummaries)用于查询备份的统计情况，返回以实例为维度的备份占用容量，以及每个实例的数据备份和日志备份的个数和容量（容量单位为字节）。"
  },
  "DescribeParamTemplateInfo": {
    "params": [
      {
        "name": "TemplateId",
        "desc": "参数模板 ID。"
      }
    ],
    "desc": "该接口（DescribeParamTemplateInfo）用于查询参数模板详情。"
  },
  "DescribeBinlogBackupOverview": {
    "params": [
      {
        "name": "Product",
        "desc": "需要查询的云数据库产品类型，目前仅支持 \"mysql\"。"
      }
    ],
    "desc": "本接口(DescribeBinlogBackupOverview)用于查询用户在当前地域总的日志备份概览。"
  },
  "DeleteAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Accounts",
        "desc": "云数据库账号。"
      }
    ],
    "desc": "本接口(DeleteAccounts)用于删除云数据库的账户。"
  },
  "DescribeDBInstanceInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID 。"
      }
    ],
    "desc": "查询实例基本信息（实例 ID ，实例名称，是否开通加密 ）"
  },
  "DescribeRollbackRangeTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表，单个实例 ID 的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeRollbackRangeTime)用于查询云数据库实例可回档的时间范围。"
  },
  "DescribeParamTemplates": {
    "params": [],
    "desc": "该接口（DescribeParamTemplates）查询参数模板列表。"
  },
  "DeleteBackup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "BackupId",
        "desc": "备份任务 ID。该任务 ID 为 [创建云数据库备份](https://cloud.tencent.com/document/api/236/15844) 接口返回的任务 ID。"
      }
    ],
    "desc": "本接口(DeleteBackup)用于删除数据库备份。本接口只支持删除手动发起的备份。"
  },
  "DescribeRoMinScale": {
    "params": [
      {
        "name": "RoInstanceId",
        "desc": "只读实例ID，格式如：cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与MasterInstanceId参数不能同时为空。"
      },
      {
        "name": "MasterInstanceId",
        "desc": "主实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，该参数与RoInstanceId参数不能同时为空。注意，当传入参数包含RoInstanceId时，返回值为只读实例升级时的最小规格；当传入参数只包含MasterInstanceId时，返回值为只读实例购买时的最小规格。"
      }
    ],
    "desc": "本接口(DescribeRoMinScale)用于获取只读实例购买、升级时的最小规格。"
  },
  "DescribeAuditConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeAuditConfig)用于查询云数据库审计策略的服务配置，包括审计日志保存时长等。"
  },
  "ModifyInstanceParam": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例短 ID 列表。"
      },
      {
        "name": "ParamList",
        "desc": "要修改的参数列表。每一个元素是 Name 和 CurrentValue 的组合。Name 是参数名，CurrentValue 是要修改成的值。"
      },
      {
        "name": "TemplateId",
        "desc": "模板id，ParamList和TemplateId必须至少传其中之一"
      },
      {
        "name": "WaitSwitch",
        "desc": "执行参数调整任务的方式，默认为 0。支持值包括：0 - 立刻执行，1 - 时间窗执行；当该值为 1 时，每次只能传一个实例（InstanceIds数量为1）"
      }
    ],
    "desc": "本接口(ModifyInstanceParam)用于修改云数据库实例的参数。"
  },
  "DescribeAsyncRequestInfo": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "异步任务的请求 ID。"
      }
    ],
    "desc": "本接口(DescribeAsyncRequestInfo)用于查询云数据库实例异步任务的执行结果。"
  },
  "DescribeDBZoneConfig": {
    "params": [],
    "desc": "本接口(DescribeDBZoneConfig)用于查询可创建的云数据库各地域可售卖的规格配置。"
  },
  "DescribeDBInstanceRebootTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。"
  },
  "DescribeDBInstances": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "项目 ID，可使用 [查询项目列表](https://cloud.tencent.com/document/product/378/4400) 接口查询项目 ID。"
      },
      {
        "name": "InstanceTypes",
        "desc": "实例类型，可取值：1 - 主实例，2 - 灾备实例，3 - 只读实例。"
      },
      {
        "name": "Vips",
        "desc": "实例的内网 IP 地址。"
      },
      {
        "name": "Status",
        "desc": "实例状态，可取值：<br>0 - 创建中<br>1 - 运行中<br>4 - 正在进行隔离操作<br>5 - 隔离中（可在回收站恢复开机）"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认值为 0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为 20，最大值为 2000。"
      },
      {
        "name": "SecurityGroupId",
        "desc": "安全组 ID。当使用安全组 ID 为过滤条件时，需指定 WithSecurityGroup 参数为 1。"
      },
      {
        "name": "PayTypes",
        "desc": "付费类型，可取值：0 - 包年包月，1 - 小时计费。"
      },
      {
        "name": "InstanceNames",
        "desc": "实例名称。"
      },
      {
        "name": "TaskStatus",
        "desc": "实例任务状态，可能取值：<br>0 - 没有任务<br>1 - 升级中<br>2 - 数据导入中<br>3 - 开放Slave中<br>4 - 外网访问开通中<br>5 - 批量操作执行中<br>6 - 回档中<br>7 - 外网访问关闭中<br>8 - 密码修改中<br>9 - 实例名修改中<br>10 - 重启中<br>12 - 自建迁移中<br>13 - 删除库表中<br>14 - 灾备实例创建同步中<br>15 - 升级待切换<br>16 - 升级切换中<br>17 - 升级切换完成<br>19 - 参数设置待执行"
      },
      {
        "name": "EngineVersions",
        "desc": "实例数据库引擎版本，可能取值：5.1、5.5、5.6 和 5.7。"
      },
      {
        "name": "VpcIds",
        "desc": "私有网络的 ID。"
      },
      {
        "name": "ZoneIds",
        "desc": "可用区的 ID。"
      },
      {
        "name": "SubnetIds",
        "desc": "子网 ID。"
      },
      {
        "name": "CdbErrors",
        "desc": "是否锁定标记。"
      },
      {
        "name": "OrderBy",
        "desc": "返回结果集排序的字段，目前支持：\"InstanceId\"，\"InstanceName\"，\"CreateTime\"，\"DeadlineTime\"。"
      },
      {
        "name": "OrderDirection",
        "desc": "返回结果集排序方式，目前支持：\"ASC\" 或者 \"DESC\"。"
      },
      {
        "name": "WithSecurityGroup",
        "desc": "是否以安全组 ID 为过滤条件。"
      },
      {
        "name": "WithExCluster",
        "desc": "是否包含独享集群详细信息，可取值：0 - 不包含，1 - 包含。"
      },
      {
        "name": "ExClusterId",
        "desc": "独享集群 ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例 ID。"
      },
      {
        "name": "InitFlag",
        "desc": "初始化标记，可取值：0 - 未初始化，1 - 初始化。"
      },
      {
        "name": "WithDr",
        "desc": "是否包含灾备关系对应的实例，可取值：0 - 不包含，1 - 包含。默认取值为1。如果拉取主实例，则灾备关系的数据在DrInfo字段中， 如果拉取灾备实例， 则灾备关系的数据在MasterInfo字段中。灾备关系中只包含部分基本的数据，详细的数据需要自行调接口拉取。"
      },
      {
        "name": "WithRo",
        "desc": "是否包含只读实例，可取值：0 - 不包含，1 - 包含。默认取值为1。"
      },
      {
        "name": "WithMaster",
        "desc": "是否包含主实例，可取值：0 - 不包含，1 - 包含。默认取值为1。"
      },
      {
        "name": "DeployGroupIds",
        "desc": "置放群组ID列表。"
      }
    ],
    "desc": "本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目 ID、实例 ID、访问地址、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。"
  },
  "VerifyRootAccount": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Password",
        "desc": "实例 ROOT 账号的密码。"
      }
    ],
    "desc": "本接口(VerifyRootAccount)用于校验云数据库实例的 ROOT 账号是否有足够的权限进行授权操作。"
  },
  "CreateAuditRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "审计规则名称。"
      },
      {
        "name": "Description",
        "desc": "审计规则描述。"
      },
      {
        "name": "RuleFilters",
        "desc": "审计规则过滤条件。若设置了过滤条件，则不会开启全审计。"
      },
      {
        "name": "AuditAll",
        "desc": "是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。"
      }
    ],
    "desc": "本接口(CreateAuditRule)用于创建用户在当前地域的审计规则。"
  },
  "DescribeDBInstanceCharset": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。"
  },
  "AssociateSecurityGroups": {
    "params": [
      {
        "name": "SecurityGroupId",
        "desc": "安全组 ID。"
      },
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表，一个或者多个实例 ID 组成的数组。"
      }
    ],
    "desc": "本接口(AssociateSecurityGroups)用于安全组批量绑定实例。"
  },
  "InitDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "NewPassword",
        "desc": "实例新的密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种。"
      },
      {
        "name": "Parameters",
        "desc": "实例的参数列表，目前支持设置“character_set_server”、“lower_case_table_names”参数。其中，“character_set_server”参数可选值为[\"utf8\",\"latin1\",\"gbk\",\"utf8mb4\"]；“lower_case_table_names”可选值为[“0”,“1”]。"
      },
      {
        "name": "Vport",
        "desc": "实例的端口，取值范围为[1024, 65535]"
      }
    ],
    "desc": "本接口(InitDBInstances)用于初始化云数据库实例，包括初始化密码、默认字符集、实例端口号等"
  },
  "ModifyAccountPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Accounts",
        "desc": "数据库的账号，包括用户名和域名。"
      },
      {
        "name": "GlobalPrivileges",
        "desc": "全局权限。其中，GlobalPrivileges 中权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\", \"PROCESS\", \"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"SHOW DATABASES\",\"CREATE TEMPORARY TABLES\",\"LOCK TABLES\",\"EXECUTE\",\"CREATE VIEW\",\"SHOW VIEW\",\"CREATE ROUTINE\",\"ALTER ROUTINE\",\"EVENT\",\"TRIGGER\"。\n注意，不传该参数表示清除该权限。"
      },
      {
        "name": "DatabasePrivileges",
        "desc": "数据库的权限。Privileges 权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\",\t\"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"CREATE TEMPORARY TABLES\",\"LOCK TABLES\",\"EXECUTE\",\"CREATE VIEW\",\"SHOW VIEW\",\"CREATE ROUTINE\",\"ALTER ROUTINE\",\"EVENT\",\"TRIGGER\"。\n注意，不传该参数表示清除该权限。"
      },
      {
        "name": "TablePrivileges",
        "desc": "数据库中表的权限。Privileges 权限的可选值为：权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\",\t\"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"CREATE VIEW\",\"SHOW VIEW\", \"TRIGGER\"。\n注意，不传该参数表示清除该权限。"
      },
      {
        "name": "ColumnPrivileges",
        "desc": "数据库表中列的权限。Privileges 权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"REFERENCES\"。\n注意，不传该参数表示清除该权限。"
      }
    ],
    "desc": "本接口(ModifyAccountPrivileges)用于修改云数据库的账户的权限信息。\n\n注意，修改账号权限时，需要传入该账号下的全量权限信息。用户可以先通过 [查询云数据库账户的权限信息\n](https://cloud.tencent.com/document/api/236/17500) 查询该账号下的全量权限信息，然后进行权限修改。"
  },
  "DescribeDBImportRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，时间格式如：2016-01-01 00:00:01。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间，时间格式如：2016-01-01 23:59:59。"
      },
      {
        "name": "Offset",
        "desc": "分页参数，偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页参数，单次请求返回的数量，默认值为20，最小值为1，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。"
  },
  "DescribeDBSwitchRecords": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值为 50，最小值为 1，最大值为 2000。"
      }
    ],
    "desc": "本接口(DescribeDBSwitchRecords)用于查询云数据库实例切换记录。"
  },
  "CreateDBImportJob": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "FileName",
        "desc": "文件名称。该文件是指用户已上传到腾讯云的文件。"
      },
      {
        "name": "User",
        "desc": "云数据库的用户名。"
      },
      {
        "name": "Password",
        "desc": "云数据库实例 User 账号的密码。"
      },
      {
        "name": "DbName",
        "desc": "导入的目标数据库名，不传表示不指定数据库。"
      }
    ],
    "desc": "本接口(CreateDBImportJob)用于创建云数据库数据导入任务。\n\n注意，用户进行数据导入任务的文件，必须提前上传到腾讯云。用户须在控制台进行文件导入。"
  },
  "DescribeAccounts": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20，最小值为1，最大值为100。"
      },
      {
        "name": "AccountRegexp",
        "desc": "匹配账号名的正则表达式，规则同 MySQL 官网。"
      }
    ],
    "desc": "本接口(DescribeAccounts)用于查询云数据库的所有账户信息。"
  },
  "DescribeAuditRules": {
    "params": [
      {
        "name": "RuleId",
        "desc": "审计规则 ID。"
      },
      {
        "name": "RuleName",
        "desc": "审计规则名称。支持按审计规则名称进行模糊匹配查询。"
      },
      {
        "name": "Limit",
        "desc": "分页大小参数。默认值为 20，最小值为 1，最大值为 100。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      }
    ],
    "desc": "本接口(DescribeAuditRules)用于查询用户在当前地域的审计规则。"
  },
  "ModifyRoGroupInfo": {
    "params": [
      {
        "name": "RoGroupId",
        "desc": "RO 组的 ID。"
      },
      {
        "name": "RoGroupInfo",
        "desc": "RO 组的详细信息。"
      },
      {
        "name": "RoWeightValues",
        "desc": "RO 组内实例的权重。若修改 RO 组的权重模式为用户自定义模式（custom），则必须设置该参数，且需要设置每个 RO 实例的权重值。"
      },
      {
        "name": "IsBalanceRoLoad",
        "desc": "是否重新均衡 RO 组内的 RO 实例的负载。支持值包括：1 - 重新均衡负载；0 - 不重新均衡负载。默认值为 0。注意，设置为重新均衡负载是，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库。"
      }
    ],
    "desc": "本接口（ModifyRoGroupInfo）用于更新云数据库只读组的信息。包括设置实例延迟超限剔除策略，设置只读实例读权重等。"
  },
  "ModifyAccountPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "NewPassword",
        "desc": "数据库账号的新密码。密码应至少包含字母、数字和字符（_+-&=!@#$%^*()）中的两种，长度为8-64个字符。"
      },
      {
        "name": "Accounts",
        "desc": "云数据库账号。"
      }
    ],
    "desc": "本接口(ModifyAccountPassword)用于修改云数据库账户的密码。"
  },
  "DescribeUploadedFiles": {
    "params": [
      {
        "name": "Path",
        "desc": "文件路径。该字段应填用户主账号的OwnerUin信息。"
      },
      {
        "name": "Offset",
        "desc": "记录偏移量，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "单次请求返回的数量，默认值为20。"
      }
    ],
    "desc": "本接口(DescribeUploadedFiles)用于查询用户导入的SQL文件列表。"
  },
  "ModifyAccountDescription": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Accounts",
        "desc": "云数据库账号。"
      },
      {
        "name": "Description",
        "desc": "数据库账号的备注信息。"
      }
    ],
    "desc": "本接口(ModifyAccountDescription)用于修改云数据库账户的备注信息。"
  },
  "DescribeSlowLogData": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间戳。"
      },
      {
        "name": "EndTime",
        "desc": "结束时间戳。"
      },
      {
        "name": "UserHosts",
        "desc": "客户端 Host 列表。"
      },
      {
        "name": "UserNames",
        "desc": "客户端 用户名 列表。"
      },
      {
        "name": "DataBases",
        "desc": "访问的 数据库 列表。"
      },
      {
        "name": "SortBy",
        "desc": "排序字段。当前支持：Timestamp,QueryTime,LockTime,RowsExamined,RowsSent 。"
      },
      {
        "name": "OrderBy",
        "desc": "升序还是降序排列。当前支持：ASC,DESC 。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0。"
      },
      {
        "name": "Limit",
        "desc": "一次性返回的记录数量，最大为400。"
      }
    ],
    "desc": "条件检索实例的慢日志。只允许查看一个月之内的慢日志"
  },
  "DeleteAuditLogFile": {
    "params": [
      {
        "name": "FileName",
        "desc": "审计日志文件名称。"
      },
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      }
    ],
    "desc": "本接口(DeleteAuditLogFile)用于删除云数据库实例的审计日志文件。"
  },
  "ModifyBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "ExpireDays",
        "desc": "备份文件的保留时间，单位为天。最小值为7天，最大值为732天。"
      },
      {
        "name": "StartTime",
        "desc": "(将废弃，建议使用 BackupTimeWindow 参数) 备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 00:00-12:00，02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。"
      },
      {
        "name": "BackupMethod",
        "desc": "自动备份方式，仅支持：physical - 物理冷备"
      },
      {
        "name": "BinlogExpireDays",
        "desc": "binlog的保留时间，单位为天。最小值为7天，最大值为732天。该值的设置不能大于备份文件的保留时间。"
      },
      {
        "name": "BackupTimeWindow",
        "desc": "备份时间窗，比如要设置每周二和周日 10:00-14:00之间备份，该参数如下：{\"Monday\": \"\", \"Tuesday\": \"10:00-14:00\", \"Wednesday\": \"\", \"Thursday\": \"\", \"Friday\": \"\", \"Saturday\": \"\", \"Sunday\": \"10:00-14:00\"}    （注：可以设置一周的某几天备份，但是每天的备份时间需要设置为相同的时间段。 如果设置了该字段，将忽略StartTime字段的设置）"
      }
    ],
    "desc": "本接口(ModifyBackupConfig)用于修改数据库备份配置信息。"
  },
  "ModifyDBInstanceProject": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 数组，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "NewProjectId",
        "desc": "项目的 ID。"
      }
    ],
    "desc": "本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。"
  },
  "DescribeBackupDatabases": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "StartTime",
        "desc": "开始时间，格式为：2017-07-12 10:29:20。"
      },
      {
        "name": "SearchDatabase",
        "desc": "要查询的数据库名前缀。"
      },
      {
        "name": "Offset",
        "desc": "分页偏移量。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，最小值为1，最大值为2000。"
      }
    ],
    "desc": "本接口(DescribeBackupDatabases)用于查询备份文件包含的库 (已废弃)。\n旧版本支持全量备份后，用户如果分库表下载逻辑备份文件，需要用到此接口。\n新版本支持(CreateBackup)创建逻辑备份的时候，直接发起指定库表备份，用户直接下载该备份文件即可。"
  },
  "DescribeDBPrice": {
    "params": [
      {
        "name": "Zone",
        "desc": "可用区信息，格式如 \"ap-guangzhou-2\"。具体能设置的值请通过 <a href=\"https://cloud.tencent.com/document/api/236/17229\">DescribeDBZoneConfig</a> 接口查询。"
      },
      {
        "name": "GoodsNum",
        "desc": "实例数量，默认值为 1，最小值 1，最大值为 100。"
      },
      {
        "name": "Memory",
        "desc": "实例内存大小，单位：MB。"
      },
      {
        "name": "Volume",
        "desc": "实例硬盘大小，单位：GB。"
      },
      {
        "name": "PayType",
        "desc": "付费类型，支持值包括：PRE_PAID - 包年包月，HOUR_PAID - 按量计费。"
      },
      {
        "name": "Period",
        "desc": "实例时长，单位：月，最小值 1，最大值为 36；查询按量计费价格时，该字段无效。"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master - 表示主实例，ro - 表示只读实例，dr - 表示灾备实例。"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，默认为 0，支持值包括：0 - 表示异步复制，1 - 表示半同步复制，2 - 表示强同步复制。"
      }
    ],
    "desc": "本接口(DescribeDBPrice)用于查询云数据库实例的价格，支持查询按量计费或者包年包月的价格。可传入实例类型、购买时长、购买数量、内存大小、硬盘大小和可用区信息等来查询实例价格。\n\n注意：对某个地域进行询价，请使用对应地域的接入点，接入点信息请参照 <a href=\"https://cloud.tencent.com/document/api/236/15832\">服务地址</a> 文档。例如：对广州地域进行询价，请把请求发到：cdb.ap-guangzhou.tencentcloudapi.com。同理对上海地域询价，把请求发到：cdb.ap-shanghai.tencentcloudapi.com。"
  },
  "ModifyAutoRenewFlag": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "AutoRenew",
        "desc": "自动续费标记，可取值的有：0 - 不自动续费，1 - 自动续费。"
      }
    ],
    "desc": "本接口(ModifyAutoRenewFlag)用于修改云数据库实例的自动续费标记。仅支持包年包月的实例设置自动续费标记。"
  },
  "RenewDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待续费的实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872)。"
      },
      {
        "name": "TimeSpan",
        "desc": "续费时长，单位：月，可选值包括 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]。"
      },
      {
        "name": "ModifyPayType",
        "desc": "如果需要将按量计费实例续费为包年包月的实例，该入参的值需要指定为 \"PREPAID\" 。"
      }
    ],
    "desc": "本接口(RenewDBInstance)用于续费云数据库实例，支持付费模式为包年包月的实例。按量计费实例可通过该接口续费为包年包月的实例。"
  },
  "StartBatchRollback": {
    "params": [
      {
        "name": "Instances",
        "desc": "用于回档的实例详情信息。"
      }
    ],
    "desc": "该接口（StartBatchRollback）用于批量回档云数据库实例的库表。"
  },
  "DescribeDeviceMonitorInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "Count",
        "desc": "返回当天最近Count个5分钟粒度的监控数据。最小值1，最大值288，不传该参数默认返回当天所有5分钟粒度监控数据。"
      }
    ],
    "desc": "本接口（DescribeDeviceMonitorInfo）用于查询云数据库物理机当天的监控信息，暂只支持内存488G、硬盘6T的实例查询。"
  },
  "OpenWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(OpenWanService)用于开通实例外网访问。\n\n注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。"
  },
  "ModifyAuditRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "审计规则 ID。"
      },
      {
        "name": "RuleName",
        "desc": "审计规则名称。"
      },
      {
        "name": "Description",
        "desc": "审计规则描述。"
      },
      {
        "name": "RuleFilters",
        "desc": "审计规则过滤条件。若设置了过滤条件，则不会开启全审计。"
      },
      {
        "name": "AuditAll",
        "desc": "是否开启全审计。支持值包括：false – 不开启全审计，true – 开启全审计。用户未设置审计规则过滤条件时，默认开启全审计。"
      }
    ],
    "desc": "本接口(ModifyAuditRule)用于修改用户的审计规则。"
  },
  "DeleteAuditRule": {
    "params": [
      {
        "name": "RuleId",
        "desc": "审计规则 ID。"
      }
    ],
    "desc": "本接口(DeleteAuditRule)用于删除用户的审计规则。"
  },
  "DescribeSupportedPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。"
  },
  "DescribeBinlogs": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      },
      {
        "name": "Offset",
        "desc": "偏移量，最小值为0。"
      },
      {
        "name": "Limit",
        "desc": "分页大小，默认值为20，最小值为1，最大值为100。"
      }
    ],
    "desc": "本接口(DescribeBinlogs)用于查询云数据库实例的 binlog 文件列表。"
  },
  "DescribeDBSecurityGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。"
  },
  "DescribeRoGroups": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdb-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeRoGroups)用于查询云数据库实例的所有的RO组的信息。"
  },
  "ModifyNameOrDescByDpId": {
    "params": [
      {
        "name": "DeployGroupId",
        "desc": "置放群组 ID。"
      },
      {
        "name": "DeployGroupName",
        "desc": "置放群组名称，最长不能超过60个字符。置放群组名和置放群组描述不能都为空。"
      },
      {
        "name": "Description",
        "desc": "置放群组描述，最长不能超过200个字符。置放群组名和置放群组描述不能都为空。"
      }
    ],
    "desc": "修改置放群组的名称或者描述"
  },
  "UpgradeDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "Memory",
        "desc": "升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的内存规格。"
      },
      {
        "name": "Volume",
        "desc": "升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口获取可升级的硬盘范围。"
      },
      {
        "name": "ProtectMode",
        "desc": "数据复制方式，支持值包括：0 - 异步复制，1 - 半同步复制，2 - 强同步复制，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "DeployMode",
        "desc": "部署模式，默认为 0，支持值包括：0 - 单可用区部署，1 - 多可用区部署，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "SlaveZone",
        "desc": "备库1的可用区信息，默认和实例的 Zone 参数一致，升级主实例为多可用区部署时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。可通过 [获取云数据库可售卖规格](https://cloud.tencent.com/document/product/236/17229) 接口查询支持的可用区。"
      },
      {
        "name": "EngineVersion",
        "desc": "主实例数据库引擎版本，支持值包括：5.5、5.6 和 5.7。"
      },
      {
        "name": "WaitSwitch",
        "desc": "切换访问新实例的方式，默认为 0。支持值包括：0 - 立刻切换，1 - 时间窗切换；当该值为 1 时，升级中过程中，切换访问新实例的流程将会在时间窗内进行，或者用户主动调用接口 [切换访问新实例](https://cloud.tencent.com/document/product/236/15864) 触发该流程。"
      },
      {
        "name": "BackupZone",
        "desc": "备库 2 的可用区信息，默认为空，升级主实例时可指定该参数，升级只读实例或者灾备实例时指定该参数无意义。"
      },
      {
        "name": "InstanceRole",
        "desc": "实例类型，默认为 master，支持值包括：master - 表示主实例，dr - 表示灾备实例，ro - 表示只读实例。"
      }
    ],
    "desc": "本接口(UpgradeDBInstance)用于升级或降级云数据库实例的配置，实例类型支持主实例、灾备实例和只读实例。"
  },
  "CreateDeployGroup": {
    "params": [
      {
        "name": "DeployGroupName",
        "desc": "置放群组名称，最长不能超过60个字符。"
      },
      {
        "name": "Description",
        "desc": "置放群组描述，最长不能超过200个字符。"
      },
      {
        "name": "Affinity",
        "desc": "置放群组的亲和性策略，目前仅支持取值为1，策略1表示同台物理机上限制实例的个数。"
      },
      {
        "name": "LimitNum",
        "desc": "置放群组亲和性策略1中同台物理机上实例的限制个数。"
      },
      {
        "name": "DevClass",
        "desc": "置放群组机型属性，可选参数：SH12+SH02、TS85。"
      }
    ],
    "desc": "本接口(CreateDeployGroup)用于创建放置实例的置放群组"
  },
  "DeleteTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DeleteTimeWindow)用于删除云数据库实例的维护时间窗口。删除实例维护时间窗口之后，默认的维护时间窗为 03:00-04:00，即当选择在维护时间窗口内切换访问新实例时，默认会在 03:00-04:00 点进行切换访问新实例。"
  }
}