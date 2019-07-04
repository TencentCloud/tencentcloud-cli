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
  "DescribeTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例ID相同。"
      }
    ],
    "desc": "本接口(DescribeTimeWindow)用于查询云数据库实例的维护时间窗口。"
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
  "DescribeBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例短实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeBackupConfig)用于查询数据库备份配置信息。"
  },
  "DescribeRollbackRangeTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例 ID 列表，单个实例Id的格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例 ID 相同。"
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
    "desc": "本接口(DeleteBackup)用于删除数据库备份。"
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
  "IsolateDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(IsolateDBInstance)用于销毁云数据库实例，销毁之后不能通过IP和端口访问数据库，按量计费实例销毁后直接下线。"
  },
  "ModifyBackupConfig": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同。"
      },
      {
        "name": "ExpireDays",
        "desc": "备份过期时间，单位为天，最小值为7天，最大值为732天。"
      },
      {
        "name": "StartTime",
        "desc": "备份时间范围，格式为：02:00-06:00，起点和终点时间目前限制为整点，目前可以选择的范围为： 02:00-06:00，06：00-10：00，10:00-14:00，14:00-18:00，18:00-22:00，22:00-02:00。"
      },
      {
        "name": "BackupMethod",
        "desc": "目标备份方法，可选的值：logical - 逻辑冷备，physical - 物理冷备；默认备份方法为 逻辑冷备。"
      }
    ],
    "desc": "本接口(ModifyBackupConfig)用于修改数据库备份配置信息。"
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
      }
    ],
    "desc": "本接口(ModifyInstanceParam)用于修改云数据库实例的参数。"
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
  "DescribeAsyncRequestInfo": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "异步任务的请求 ID。"
      }
    ],
    "desc": "本接口(DescribeAsyncRequestInfo)用于查询云数据库实例异步任务的执行结果。"
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
        "desc": "mysql版本。"
      },
      {
        "name": "TemplateId",
        "desc": "源参数模板ID。"
      },
      {
        "name": "ParamList",
        "desc": "参数列表。"
      }
    ],
    "desc": "该接口（CreateParamTemplate）用于创建参数模板。"
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
      }
    ],
    "desc": "本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。\n\n该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为 1，且 TaskStatus 为 0，表示实例已经发货成功。\n\n1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；\n2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；\n3. 支持创建 MySQL 5.5、MySQL 5.6 和 MySQL 5.7 版本；\n4. 支持创建主实例、灾备实例和只读实例；\n5. 当入参指定 Port，ParamList 或 Password 时，该实例会进行初始化操作；"
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
  "DescribeDBZoneConfig": {
    "params": [],
    "desc": "本接口(DescribeDBZoneConfig)用于查询可创建的云数据库各地域可售卖的规格配置。"
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
  "DescribeDBInstanceRebootTime": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例的 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。"
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
    "desc": "本接口(DescribeBackupTables)用于查询指定的数据库的备份数据表名 (将废弃)。"
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
        "desc": "安全组 ID。"
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
        "desc": "实例任务状态，可能取值：<br>0 - 没有任务<br>1 - 升级中<br>2 - 数据导入中<br>3 - 开放Slave中<br>4 - 外网访问开通中<br>5 - 批量操作执行中<br>6 - 回档中<br>7 - 外网访问关闭中<br>8 - 密码修改中<br>9 - 实例名修改中<br>10 - 重启中<br>12 - 自建迁移中<br>13 - 删除库表中<br>14 - 灾备实例创建同步中<br>15 - 升级待切换<br>16 - 升级切换中<br>17 - 升级切换完成"
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
        "desc": "是否包含安全组详细信息，可取值：0 - 不包含，1 - 包含。"
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
        "desc": "是否包含灾备实例，可取值：0 - 不包含，1 - 包含。"
      },
      {
        "name": "WithRo",
        "desc": "是否包含只读实例，可取值：0 - 不包含，1 - 包含。"
      },
      {
        "name": "WithMaster",
        "desc": "是否包含主实例，可取值：0 - 不包含，1 - 包含。"
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
  "DescribeDefaultParams": {
    "params": [
      {
        "name": "EngineVersion",
        "desc": "mysql版本，目前支持 [\"5.1\", \"5.5\", \"5.6\", \"5.7\"]。"
      }
    ],
    "desc": "该接口（DescribeDefaultParams）用于查询默认的可设置参数列表。"
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
      }
    ],
    "desc": "本接口(RenewDBInstance)用于续费云数据库实例，仅支持付费模式为包年包月的实例。按量计费实例不需要续费。"
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
  "StartBatchRollback": {
    "params": [
      {
        "name": "Instances",
        "desc": "用于回档的实例详情信息。"
      }
    ],
    "desc": "该接口（StartBatchRollback）用于批量回档云数据库实例的库表。"
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
        "desc": "全局权限。其中，GlobalPrivileges 中权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\",\t\"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"SHOW DATABASES\",\"CREATE TEMPORARY TABLES\",\"LOCK TABLES\",\"EXECUTE\",\"CREATE VIEW\",\"SHOW VIEW\",\"CREATE ROUTINE\",\"ALTER ROUTINE\",\"EVENT\",\"TRIGGER\"。"
      },
      {
        "name": "DatabasePrivileges",
        "desc": "数据库的权限。Privileges 权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\",\t\"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"CREATE TEMPORARY TABLES\",\"LOCK TABLES\",\"EXECUTE\",\"CREATE VIEW\",\"SHOW VIEW\",\"CREATE ROUTINE\",\"ALTER ROUTINE\",\"EVENT\",\"TRIGGER\"。"
      },
      {
        "name": "TablePrivileges",
        "desc": "数据库中表的权限。Privileges 权限的可选值为：权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"DELETE\",\"CREATE\",\t\"DROP\",\"REFERENCES\",\"INDEX\",\"ALTER\",\"CREATE VIEW\",\"SHOW VIEW\", \"TRIGGER\"。"
      },
      {
        "name": "ColumnPrivileges",
        "desc": "数据库表中列的权限。Privileges 权限的可选值为：\"SELECT\",\"INSERT\",\"UPDATE\",\"REFERENCES\"。"
      }
    ],
    "desc": "本接口(ModifyAccountPrivileges)用于修改云数据库的账户的权限信息。"
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
      }
    ],
    "desc": "本接口(DescribeAccounts)用于查询云数据库的所有账户信息。"
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
  "SwitchForUpgrade": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      },
      {
        "name": "AsyncRequestId",
        "desc": "异步任务请求 ID，执行 CDB 相关操作返回的 AsyncRequestId。"
      },
      {
        "name": "TaskTypes",
        "desc": "任务类型，不传值则查询所有任务类型，可能的值：1-数据库回档；2-SQL操作；3-数据导入；5-参数设置；6-初始化；7-重启；8-开启GTID；9-只读实例升级；10-数据库批量回档；11-主实例升级；12-删除库表；13-切换为主实例。"
      },
      {
        "name": "TaskStatus",
        "desc": "任务状态，不传值则查询所有任务状态，可能的值：-1-未定义；0-初始化; 1-运行中；2-执行成功；3-执行失败；4-已终止；5-已删除；6-已暂停。"
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
  "DescribeSupportedPrivileges": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。"
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
    "desc": "本接口(DescribeBinlogs)用于查询云数据库实例的二进制数据。"
  },
  "DescribeTagsOfInstanceIds": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "实例列表。"
      },
      {
        "name": "Offset",
        "desc": "偏移量。"
      },
      {
        "name": "Limit",
        "desc": "每页返回多少个标签。"
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
        "desc": "匹配数据库库名的正则表达式，规则同 MySQL 官网"
      }
    ],
    "desc": "本接口(DescribeDatabases)用于查询云数据库实例的数据库信息。"
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
  "DescribeInstanceParams": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "该接口（DescribeInstanceParams）用于查询实例的参数列表。"
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
  "OpenWanService": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同，可使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值。"
      }
    ],
    "desc": "本接口(OpenWanService)用于开通实例外网访问。\n\n注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。"
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
    "desc": "本接口(UpgradeDBInstance)用于升级云数据库实例，实例类型支持主实例、灾备实例和只读实例。"
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
      }
    ],
    "desc": "本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。"
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
  "DeleteTimeWindow": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，格式如：cdb-c1nl9rpv 或者 cdbro-c1nl9rpv，与云数据库控制台页面中显示的实例 ID 相同。"
      }
    ],
    "desc": "本接口(DeleteTimeWindow)用于删除云数据库实例的维护时间窗口。删除实例维护时间窗口之后，默认的维护时间窗为 03:00-04:00，即当选择在维护时间窗口内切换访问新实例时，默认会在 03:00-04:00 点进行切换访问新实例。"
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
    "desc": "本接口(DescribeBackupDatabases)用于查询备份数据库列表 (将废弃)。"
  }
}