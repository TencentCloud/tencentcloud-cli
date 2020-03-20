# -*- coding: utf-8 -*-
DESC = "dts-2018-03-30"
INFO = {
  "DeleteSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "待删除的灾备同步任务ID"
      }
    ],
    "desc": "删除灾备同步任务 （运行中的同步任务不能删除）。"
  },
  "DescribeSyncJobs": {
    "params": [
      {
        "name": "JobId",
        "desc": "灾备同步任务ID"
      },
      {
        "name": "JobName",
        "desc": "灾备同步任务名"
      },
      {
        "name": "Order",
        "desc": "排序字段，可以取值为JobId、Status、JobName、CreateTime"
      },
      {
        "name": "OrderSeq",
        "desc": "排序方式，升序为ASC，降序为DESC"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回实例数量，默认20，有效区间[1,100]"
      }
    ],
    "desc": "查询在迁移平台发起的灾备同步任务"
  },
  "ActivateSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "订阅实例ID。"
      },
      {
        "name": "InstanceId",
        "desc": "数据库实例ID"
      },
      {
        "name": "SubscribeObjectType",
        "desc": "数据订阅类型0-全实例订阅，1数据订阅，2结构订阅，3数据订阅与结构订阅"
      },
      {
        "name": "Objects",
        "desc": "订阅对象"
      },
      {
        "name": "UniqSubnetId",
        "desc": "数据订阅服务所在子网。默认为数据库实例所在的子网内。"
      },
      {
        "name": "Vport",
        "desc": "订阅服务端口；默认为7507"
      }
    ],
    "desc": "本接口用于配置数据订阅，只有在未配置状态的订阅实例才能调用此接口。"
  },
  "ModifySyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "待修改的灾备同步任务ID"
      },
      {
        "name": "JobName",
        "desc": "灾备同步任务名称"
      },
      {
        "name": "SyncOption",
        "desc": "灾备同步任务配置选项"
      },
      {
        "name": "DatabaseInfo",
        "desc": "当选择'指定库表'灾备同步的时候, 需要设置待同步的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。\n对于database-table两级结构的数据库：\n[{\"Database\":\"db1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\"}]"
      }
    ],
    "desc": "修改灾备同步任务. \n当同步任务处于下述状态时, 允许调用本接口: 同步任务创建中, 创建完成, 校验成功, 校验失败. \n源实例和目标实例信息不允许修改，可以修改任务名、需要同步的库表。"
  },
  "CreateSyncJob": {
    "params": [
      {
        "name": "JobName",
        "desc": "灾备同步任务名"
      },
      {
        "name": "SyncOption",
        "desc": "灾备同步任务配置选项"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "源实例数据库类型，目前仅包括：mysql"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型，目前仅包括：cdb(云上cdb实例)"
      },
      {
        "name": "SrcInfo",
        "desc": "源实例信息"
      },
      {
        "name": "DstDatabaseType",
        "desc": "目标实例数据库类型，目前仅包括：mysql"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，目前仅包括：cdb(云上cdb实例)"
      },
      {
        "name": "DstInfo",
        "desc": "目标实例信息"
      },
      {
        "name": "DatabaseInfo",
        "desc": "需要同步的源数据库表信息，用json格式的字符串描述。\n对于database-table两级结构的数据库：\n[{Database:db1,Table:[table1,table2]},{Database:db2}]"
      }
    ],
    "desc": "本接口(CreateSyncJob)用于创建灾备同步任务。\n创建同步任务后，可以通过 CreateSyncCheckJob 接口发起校验任务。校验成功后才可以通过 StartSyncJob 接口启动同步任务。"
  },
  "ModifySubscribeObjects": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      },
      {
        "name": "SubscribeObjectType",
        "desc": "数据订阅的类型，可选的值有：0 - 全实例订阅；1 - 数据订阅；2 - 结构订阅；3 - 数据订阅+结构订阅"
      },
      {
        "name": "Objects",
        "desc": "订阅的数据库表信息"
      }
    ],
    "desc": "本接口(ModifySubscribeObjects)用于修改数据订阅通道的订阅规则"
  },
  "StartSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "灾备同步任务ID"
      }
    ],
    "desc": "创建的灾备同步任务在通过 CreateSyncCheckJob 和 DescribeSyncCheckJob 确定校验成功后，可以调用该接口启动同步"
  },
  "DeleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "本接口（DeleteMigrationJob）用于删除数据迁移任务。当通过DescribeMigrateJobs接口查询到任务的状态为：检验中（status=3）、运行中（status=7）、准备完成（status=8）、撤销中（status=11）或者完成中（status=12）时，不允许删除任务。"
  },
  "DescribeAsyncRequestInfo": {
    "params": [
      {
        "name": "AsyncRequestId",
        "desc": "任务 ID"
      }
    ],
    "desc": "本接口（DescribeAsyncRequestInfo）用于查询任务执行结果"
  },
  "SwitchDrToMaster": {
    "params": [
      {
        "name": "DstInfo",
        "desc": "灾备实例的信息"
      },
      {
        "name": "DatabaseType",
        "desc": "数据库的类型  （如 mysql）"
      }
    ],
    "desc": "将灾备升级为主实例，停止从原来所属主实例的同步，断开主备关系。"
  },
  "StopMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "本接口（StopMigrateJob）用于撤销数据迁移任务。\n在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败。通过DescribeMigrateJobs接口查询到任务状态为运行中（status=7）或准备完成（status=8）时，才能撤销数据迁移任务。"
  },
  "DescribeRegionConf": {
    "params": [],
    "desc": "本接口（DescribeRegionConf）用于查询可售卖订阅实例的地域"
  },
  "DescribeMigrateJobs": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      },
      {
        "name": "JobName",
        "desc": "数据迁移任务名称"
      },
      {
        "name": "Order",
        "desc": "排序字段，可以取值为JobId、Status、JobName、MigrateType、RunMode、CreateTime"
      },
      {
        "name": "OrderSeq",
        "desc": "排序方式，升序为ASC，降序为DESC"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回实例数量，默认20，有效区间[1,100]"
      }
    ],
    "desc": "查询数据迁移任务.\n如果是金融区链路, 请使用域名: https://dts.ap-shenzhen-fsi.tencentcloudapi.com"
  },
  "DescribeSubscribes": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅的实例ID"
      },
      {
        "name": "SubscribeName",
        "desc": "数据订阅的实例名称"
      },
      {
        "name": "InstanceId",
        "desc": "绑定数据库实例的ID"
      },
      {
        "name": "ChannelId",
        "desc": "数据订阅实例的通道ID"
      },
      {
        "name": "PayType",
        "desc": "计费模式筛选，可能的值：0-包年包月，1-按量计费"
      },
      {
        "name": "Product",
        "desc": "订阅的数据库产品，如mysql"
      },
      {
        "name": "Status",
        "desc": "数据订阅实例的状态，creating - 创建中，normal - 正常运行，isolating - 隔离中，isolated - 已隔离，offlining - 下线中"
      },
      {
        "name": "SubsStatus",
        "desc": "数据订阅实例的配置状态，unconfigure - 未配置， configuring - 配置中，configured - 已配置"
      },
      {
        "name": "Offset",
        "desc": "返回记录的起始偏移量"
      },
      {
        "name": "Limit",
        "desc": "单次返回的记录数量"
      },
      {
        "name": "OrderDirection",
        "desc": "排序方向，可选的值为\"DESC\"和\"ASC\"，默认为\"DESC\"，按创建时间逆序排序"
      }
    ],
    "desc": "本接口(DescribeSubscribes)获取数据订阅实例信息列表，默认分页，每次返回20条"
  },
  "DescribeSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "要查询的灾备同步任务ID"
      }
    ],
    "desc": "本接口用于在通过 CreateSyncCheckJob 接口创建灾备同步校验任务后，获取校验的结果。能查询到当前校验的状态和进度。\n若通过校验, 则可调用 StartSyncJob 启动同步任务。\n若未通过校验, 则会返回校验失败的原因。 可通过 ModifySyncJob 修改配置，然后再次发起校验。\n校验任务需要大概约30秒，当返回的 Status 不为 finished 时表示尚未校验完成，需要轮询该接口。\n如果 Status=finished 且 CheckFlag=1 时表示校验成功。\n如果 Status=finished 且 CheckFlag !=1 时表示校验失败。"
  },
  "CreateMigrateJob": {
    "params": [
      {
        "name": "JobName",
        "desc": "数据迁移任务名称"
      },
      {
        "name": "MigrateOption",
        "desc": "迁移任务配置选项"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "源实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(腾讯云数据库实例),ccn(云联网实例)"
      },
      {
        "name": "SrcInfo",
        "desc": "源实例信息，具体内容跟迁移任务类型相关"
      },
      {
        "name": "DstDatabaseType",
        "desc": "目标实例数据库类型，目前支持：mysql，redis，mongodb，postgresql，mariadb，percona。不同地域数据库类型的具体支持情况，请参考控制台创建迁移页面。"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，目前支持：cdb（腾讯云数据库实例）"
      },
      {
        "name": "DstInfo",
        "desc": "目标实例信息"
      },
      {
        "name": "DatabaseInfo",
        "desc": "需要迁移的源数据库表信息，用json格式的字符串描述。当MigrateOption.MigrateObject配置为2（指定库表迁移）时必填。\n对于database-table两级结构的数据库：\n[{Database:db1,Table:[table1,table2]},{Database:db2}]\n对于database-schema-table三级结构：\n[{Database:db1,Schema:s1\nTable:[table1,table2]},{Database:db1,Schema:s2\nTable:[table1,table2]},{Database:db2,Schema:s1\nTable:[table1,table2]},{Database:db3},{Database:db4\nSchema:s1}]"
      }
    ],
    "desc": "本接口（CreateMigrateJob）用于创建数据迁移任务。\n\n如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com"
  },
  "ModifySubscribeVipVport": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      },
      {
        "name": "DstUniqSubnetId",
        "desc": "指定目的子网，如果传此参数，DstIp必须在目的子网内"
      },
      {
        "name": "DstIp",
        "desc": "目标IP，与DstPort至少传一个"
      },
      {
        "name": "DstPort",
        "desc": "目标PORT，支持范围为：[1025-65535]"
      }
    ],
    "desc": "本接口(ModifySubscribeVipVport)用于修改数据订阅实例的IP和端口号"
  },
  "CreateMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "创建校验迁移任务\n在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.\n校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移."
  },
  "ModifySubscribeConsumeTime": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      },
      {
        "name": "ConsumeStartTime",
        "desc": "消费时间起点，也即是指定订阅数据的时间起点，时间格式如：Y-m-d h:m:s，取值范围为过去24小时之内"
      }
    ],
    "desc": "本接口(ModifySubscribeConsumeTime)用于修改数据订阅通道的消费时间点"
  },
  "ModifySubscribeName": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      },
      {
        "name": "SubscribeName",
        "desc": "数据订阅实例的名称，长度限制为[1,60]"
      }
    ],
    "desc": "本接口(ModifySubscribeName)用于修改数据订阅实例的名称"
  },
  "CreateSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "灾备同步任务ID"
      }
    ],
    "desc": "在调用 StartSyncJob 接口启动灾备同步前, 必须调用本接口创建校验, 且校验成功后才能开始同步数据. 校验的结果可以通过 DescribeSyncCheckJob 查看.\n校验成功后才能启动同步."
  },
  "CreateSubscribe": {
    "params": [
      {
        "name": "Product",
        "desc": "订阅的数据库类型，目前支持的有 mysql"
      },
      {
        "name": "PayType",
        "desc": "实例付费类型，1小时计费，0包年包月"
      },
      {
        "name": "Duration",
        "desc": "购买时长。PayType为0时必填。单位为月，最大支持120"
      },
      {
        "name": "Count",
        "desc": "购买数量,默认为1，最大为10"
      },
      {
        "name": "AutoRenew",
        "desc": "是否自动续费，默认为0，1表示自动续费。小时计费实例设置该标识无效。"
      }
    ],
    "desc": "本接口(CreateSubscribe)用于创建一个数据订阅实例。"
  },
  "ResetSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      }
    ],
    "desc": "本接口(ResetSubscribe)用于重置数据订阅实例，已经激活的数据订阅实例，重置后可以使用ActivateSubscribe接口绑定其他的数据库实例"
  },
  "StartMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "本接口（StartMigrationJob）用于启动迁移任务。非定时迁移任务会在调用后立即开始迁移，定时任务则会开始倒计时。\n调用此接口前，请务必先使用CreateMigrateCheckJob校验数据迁移任务，并通过DescribeMigrateJobs接口查询到任务状态为校验通过（status=4）时，才能启动数据迁移任务。"
  },
  "ModifyMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "待修改的数据迁移任务ID"
      },
      {
        "name": "JobName",
        "desc": "数据迁移任务名称"
      },
      {
        "name": "MigrateOption",
        "desc": "迁移任务配置选项"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例),cdb(云上CDB实例)"
      },
      {
        "name": "SrcInfo",
        "desc": "源实例信息，具体内容跟迁移任务类型相关"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，值包括：extranet(外网),cvm(CVM自建实例),dcg(专线接入的实例),vpncloud(云VPN接入的实例)，cdb(云上CDB实例). 目前只支持cdb."
      },
      {
        "name": "DstInfo",
        "desc": "目标实例信息, 其中目标实例地域不允许修改."
      },
      {
        "name": "DatabaseInfo",
        "desc": "当选择'指定库表'迁移的时候, 需要设置待迁移的源数据库表信息,用符合json数组格式的字符串描述, 如下所例。\n\n对于database-table两级结构的数据库：\n[{\"Database\":\"db1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\"}]\n对于database-schema-table三级结构：\n[{\"Database\":\"db1\",\"Schema\":\"s1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db1\",\"Schema\":\"s2\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db2\",\"Schema\":\"s1\",\"Table\":[\"table1\",\"table2\"]},{\"Database\":\"db3\"},{\"Database\":\"db4\",\"Schema\":\"s1\"}]\n\n如果是'整个实例'的迁移模式,不需设置该字段"
      }
    ],
    "desc": "本接口（ModifyMigrateJob）用于修改数据迁移任务。\n当迁移任务处于下述状态时，允许调用本接口修改迁移任务：迁移创建中（status=1）、 校验成功(status=4)、校验失败(status=5)、迁移失败(status=10)。但源实例、目标实例类型和目标实例地域不允许修改。\n\n如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com"
  },
  "OfflineIsolatedSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "数据订阅实例的ID"
      }
    ],
    "desc": "本接口（OfflineIsolatedSubscribe）用于下线已隔离的数据订阅实例"
  },
  "IsolateSubscribe": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "订阅实例ID"
      }
    ],
    "desc": "本接口（IsolateSubscribe）用于隔离小时计费的订阅实例。调用后，订阅实例将不能使用，同时停止计费。"
  },
  "DescribeSubscribeConf": {
    "params": [
      {
        "name": "SubscribeId",
        "desc": "订阅实例ID"
      }
    ],
    "desc": "本接口（DescribeSubscribeConf）用于查询订阅实例配置"
  },
  "DescribeMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "本接口用于创建校验后,获取校验的结果. 能查询到当前校验的状态和进度. \n若通过校验, 则可调用'StartMigrateJob' 开始迁移.\n若未通过校验, 则能查询到校验失败的原因. 请按照报错, 通过'ModifyMigrateJob'修改迁移配置或是调整源/目标实例的相关参数."
  },
  "CompleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "本接口（CompleteMigrateJob）用于完成数据迁移任务。\n选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据。\n通过DescribeMigrateJobs接口查询到任务的状态为准备完成（status=8）时，此时可以调用本接口完成迁移任务。\n"
  }
}