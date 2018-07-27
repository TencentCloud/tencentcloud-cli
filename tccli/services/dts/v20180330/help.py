# -*- coding: utf-8 -*-
DESC = "dts-2018-03-30"
INFO = {
  "CreateMigrateCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "创建校验迁移任务\n在开始迁移前, 必须调用本接口创建校验, 且校验成功后才能开始迁移. 校验的结果可以通过DescribeMigrateCheckJob查看.\n校验成功后,迁移任务若有修改, 则必须重新创建校验并通过后, 才能开始迁移."
  },
  "CreateSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "灾备同步任务ID"
      }
    ],
    "desc": "在开始灾备同步前, 必须调用本接口创建校验, 且校验成功后才能开始同步数据. 校验的结果可以通过DescribeSyncCheckJob查看.\n校验成功或失败后均可再修改, 修改后必须重新校验并通过后, 才能开始同步."
  },
  "StartMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "非定时任务会在调用后立即开始迁移，定时任务则会开始倒计时。\n调用此接口前，请务必先校验数据迁移任务通过。"
  },
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
        "desc": "源实例数据库类型:mysql,redis,mongodb"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)"
      },
      {
        "name": "SrcInfo",
        "desc": "源实例信息，具体内容跟迁移任务类型相关"
      },
      {
        "name": "DstDatabaseType",
        "desc": "目标实例数据库类型,mysql,redis,mongodb"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例). 目前只支持cdb."
      },
      {
        "name": "DstInfo",
        "desc": "目标实例信息"
      },
      {
        "name": "DatabaseInfo",
        "desc": "需要迁移的源数据库表信息，用json格式的字符串描述。\n对于database-table两级结构的数据库：\n[{Database:db1,Table:[table1,table2]},{Database:db2}]\n对于database-schema-table三级结构：\n[{Database:db1,Schema:s1\nTable:[table1,table2]},{Database:db1,Schema:s2\nTable:[table1,table2]},{Database:db2,Schema:s1\nTable:[table1,table2]},{Database:db3},{Database:db4\nSchema:s1}]"
      }
    ],
    "desc": "本接口用于创建数据迁移任务。\n\n如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com"
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
  "DeleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "删除数据迁移任务. 正在校验和正在迁移的任务不允许删除"
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
    "desc": "本接口(CreateSyncJob)用于创建灾备同步任务。"
  },
  "StopMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "撤销数据迁移任务.\n在迁移过程中允许调用该接口撤销迁移, 撤销迁移的任务会失败."
  },
  "CompleteMigrateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "数据迁移任务ID"
      }
    ],
    "desc": "完成数据迁移任务.\n选择采用增量迁移方式的任务, 需要在迁移进度进入准备完成阶段后, 调用本接口, 停止迁移增量数据.\n只有当正在迁移的任务, 进入了准备完成阶段, 才能调用本接口完成迁移."
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
        "desc": "源实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例)"
      },
      {
        "name": "SrcInfo",
        "desc": "源实例信息，具体内容跟迁移任务类型相关"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型，值包括：extranet(外网),cvm(cvm自建实例),dcg(专线接入的实例),vpncloud(云vpn接入的实例),vpnselfbuild(自建vpn接入的实例)，cdb(云上cdb实例). 目前只支持cdb."
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
    "desc": "修改数据迁移任务. \n当迁移任务处于下述状态时, 允许调用本接口: 迁移创建中, 创建完成, 校验成功, 校验失败, 迁移失败. \n源实例和目标实例类型不允许修改, 目标实例地域不允许修改。\n\n如果是金融区链路, 请使用域名: dts.ap-shenzhen-fsi.tencentcloudapi.com"
  },
  "StartSyncJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "灾备同步任务ID"
      }
    ],
    "desc": "创建的灾备同步任务在校验成功后，可以调用该接口开始同步"
  },
  "DescribeSyncCheckJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "要查询的灾备同步任务ID"
      }
    ],
    "desc": "本接口用于创建灾备同步校验任务后,获取校验的结果. 能查询到当前校验的状态和进度. \n若通过校验, 则可调用'StartSyncJob' 开始迁移.\n若未通过校验, 则会返回校验失败的原因. 可通过'ModifySyncJob'修改配置重新发起校验."
  }
}