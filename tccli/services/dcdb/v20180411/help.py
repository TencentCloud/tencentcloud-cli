# -*- coding: utf-8 -*-
DESC = "dcdb-2018-04-11"
INFO = {
  "DescribeDCDBSaleInfo": {
    "params": [],
    "desc": "本接口(DescribeDCDBSaleInfo)用于查询分布式数据库可售卖的地域和可用区信息。"
  },
  "DescribeDCDBPrice": {
    "params": [
      {
        "name": "Zone",
        "desc": "欲新购实例的可用区ID。"
      },
      {
        "name": "Count",
        "desc": "欲购买实例的数量，目前只支持购买1个实例"
      },
      {
        "name": "Period",
        "desc": "欲购买的时长，单位：月。"
      },
      {
        "name": "ShardNodeCount",
        "desc": "单个分片节点个数大小，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardMemory",
        "desc": "分片内存大小，单位：GB，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardStorage",
        "desc": "分片存储空间大小，单位：GB，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardCount",
        "desc": "实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。"
      }
    ],
    "desc": "本接口（DescribeDCDBPrice）用于在购买实例前，查询实例的价格。"
  },
  "CreateDCDBInstance": {
    "params": [
      {
        "name": "Zones",
        "desc": "分片节点可用区分布，最多可填两个可用区。当分片规格为一主两从时，其中两个节点在第一个可用区。"
      },
      {
        "name": "Count",
        "desc": "欲购买实例的数量，目前只支持购买1个实例"
      },
      {
        "name": "Period",
        "desc": "欲购买的时长，单位：月。"
      },
      {
        "name": "ProjectId",
        "desc": "项目 ID，可以通过查看项目列表获取，不传则关联到默认项目"
      },
      {
        "name": "VpcId",
        "desc": "虚拟私有网络 ID，不传或传空表示创建为基础网络"
      },
      {
        "name": "SubnetId",
        "desc": "虚拟私有网络子网 ID，VpcId不为空时必填"
      },
      {
        "name": "ShardMemory",
        "desc": "分片内存大小，单位：GB，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardStorage",
        "desc": "分片存储空间大小，单位：GB，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardNodeCount",
        "desc": "单个分片节点个数，可以通过 DescribeShardSpec\n 查询实例规格获得。"
      },
      {
        "name": "ShardCount",
        "desc": "实例分片个数，可选范围2-8，可以通过升级实例进行新增分片到最多64个分片。"
      },
      {
        "name": "DbVersionId",
        "desc": "数据库引擎版本，当前可选：10.0.10，10.1.9，5.7.17"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      }
    ],
    "desc": "本接口（CreateDCDBInstance）用于创建包年包月的云数据库实例，可通过传入实例规格、数据库版本号、购买时长等信息创建云数据库实例。"
  },
  "RenewDCDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。"
      },
      {
        "name": "Period",
        "desc": "续费时长，单位：月。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      }
    ],
    "desc": "本接口（RenewDCDBInstance）用于续费分布式数据库实例。"
  },
  "DescribeShardSpec": {
    "params": [],
    "desc": "查询可创建的分布式数据库可售卖的分片规格配置。"
  },
  "DescribeDCDBUpgradePrice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。"
      },
      {
        "name": "UpgradeType",
        "desc": "升级类型，取值范围: \n<li> ADD: 新增分片 </li> \n <li> EXPAND: 升级实例中的已有分片 </li> \n <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>"
      },
      {
        "name": "AddShardConfig",
        "desc": "新增分片配置，当UpgradeType为ADD时生效。"
      },
      {
        "name": "ExpandShardConfig",
        "desc": "扩容分片配置，当UpgradeType为EXPAND时生效。"
      },
      {
        "name": "SplitShardConfig",
        "desc": "切分分片配置，当UpgradeType为SPLIT时生效。"
      }
    ],
    "desc": "本接口（DescribeDCDBUpgradePrice）用于查询升级分布式数据库实例价格。"
  },
  "DescribeDCDBInstances": {
    "params": [
      {
        "name": "InstanceIds",
        "desc": "按照一个或者多个实例 ID 查询。实例 ID 形如：dcdbt-2t4cf98d"
      },
      {
        "name": "SearchName",
        "desc": "搜索的字段名，当前支持的值有：instancename、vip、all。传 instancename 表示按实例名进行搜索；传 vip 表示按内网IP进行搜索；传 all 将会按实例ID、实例名和内网IP进行搜索。"
      },
      {
        "name": "SearchKey",
        "desc": "搜索的关键字，支持模糊搜索。多个关键字使用换行符（'\\n'）分割。"
      },
      {
        "name": "ProjectIds",
        "desc": "按项目 ID 查询"
      },
      {
        "name": "IsFilterVpc",
        "desc": "是否根据 VPC 网络来搜索，0 为否，1 为是"
      },
      {
        "name": "VpcId",
        "desc": "私有网络 ID， IsFilterVpc 为 1 时有效"
      },
      {
        "name": "SubnetId",
        "desc": "私有网络的子网 ID， IsFilterVpc 为 1 时有效"
      },
      {
        "name": "OrderBy",
        "desc": "排序字段， projectId， createtime， instancename 三者之一"
      },
      {
        "name": "OrderByType",
        "desc": "排序类型， desc 或者 asc"
      },
      {
        "name": "Offset",
        "desc": "偏移量，默认为 0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认为 10，最大值为 100。"
      }
    ],
    "desc": "查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。\n如果不指定任何筛选条件，则默认返回10条实例记录，单次请求最多支持返回100条实例记录。"
  },
  "DescribeDBLogFiles": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID，形如：dcdbt-ow7t8lmc。"
      },
      {
        "name": "ShardId",
        "desc": "分片 ID，形如：shard-7noic7tv"
      },
      {
        "name": "Type",
        "desc": "请求日志类型，取值只能为1、2、3或者4。1-binlog，2-冷备，3-errlog，4-slowlog。"
      }
    ],
    "desc": "本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。"
  },
  "DescribeOrders": {
    "params": [
      {
        "name": "DealNames",
        "desc": "待查询的长订单号列表，创建实例、续费实例、扩容实例接口返回。"
      }
    ],
    "desc": "本接口（DescribeOrders）用于查询分布式数据库订单信息。传入订单Id来查询订单关联的分布式数据库实例，和对应的任务流程ID。"
  },
  "UpgradeDCDBInstance": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待升级的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。"
      },
      {
        "name": "UpgradeType",
        "desc": "升级类型，取值范围: \n<li> ADD: 新增分片 </li> \n <li> EXPAND: 升级实例中的已有分片 </li> \n <li> SPLIT: 将已有分片中的数据切分到新增分片上</li>"
      },
      {
        "name": "AddShardConfig",
        "desc": "新增分片配置，当UpgradeType为ADD时生效。"
      },
      {
        "name": "ExpandShardConfig",
        "desc": "扩容分片配置，当UpgradeType为EXPAND时生效。"
      },
      {
        "name": "SplitShardConfig",
        "desc": "切分分片配置，当UpgradeType为SPLIT时生效。"
      },
      {
        "name": "AutoVoucher",
        "desc": "是否自动使用代金券进行支付，默认不使用。"
      },
      {
        "name": "VoucherIds",
        "desc": "代金券ID列表，目前仅支持指定一张代金券。"
      }
    ],
    "desc": "本接口（UpgradeDCDBInstance）用于升级分布式数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。"
  },
  "DescribeDCDBRenewalPrice": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "待续费的实例ID。形如：dcdbt-ow728lmc，可以通过 DescribeDCDBInstances 查询实例详情获得。"
      },
      {
        "name": "Period",
        "desc": "续费时长，单位：月。不传则默认为1个月。"
      }
    ],
    "desc": "本接口（DescribeDCDBRenewalPrice）用于在续费分布式数据库实例时，查询续费的价格。"
  }
}