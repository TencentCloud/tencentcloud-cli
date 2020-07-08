# -*- coding: utf-8 -*-
DESC = "ckafka-2019-08-19"
INFO = {
  "DescribeRoute": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例唯一id"
      }
    ],
    "desc": "查看路由信息"
  },
  "DescribeGroupInfo": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "（过滤条件）按照实例 ID 过滤。"
      },
      {
        "name": "GroupList",
        "desc": "Kafka 消费分组，Consumer-group，这里是数组形式，格式：GroupList.0=xxx&GroupList.1=yyy。"
      }
    ],
    "desc": "获取消费分组信息"
  },
  "CreateAcl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id信息"
      },
      {
        "name": "ResourceType",
        "desc": "Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "ResourceName",
        "desc": "资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称"
      },
      {
        "name": "Operation",
        "desc": "Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS)"
      },
      {
        "name": "PermissionType",
        "desc": "权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "Host",
        "desc": "默认为\\*，表示任何host都可以访问，当前ckafka不支持host为\\*，但是后面开源kafka的产品化会直接支持"
      },
      {
        "name": "Principal",
        "desc": "用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户"
      }
    ],
    "desc": "添加 ACL 策略"
  },
  "ModifyTopicAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID。"
      },
      {
        "name": "TopicName",
        "desc": "主题名称。"
      },
      {
        "name": "Note",
        "desc": "主题备注，是一个不超过64个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线-。"
      },
      {
        "name": "EnableWhiteList",
        "desc": "IP 白名单开关，1：打开；0：关闭。"
      },
      {
        "name": "MinInsyncReplicas",
        "desc": "默认为1。"
      },
      {
        "name": "UncleanLeaderElectionEnable",
        "desc": "默认为 0，0：false；1：true。"
      },
      {
        "name": "RetentionMs",
        "desc": "消息保留时间，单位：ms，当前最小值为60000ms。"
      },
      {
        "name": "SegmentMs",
        "desc": "Segment 分片滚动的时长，单位：ms，当前最小为86400000ms。"
      },
      {
        "name": "MaxMessageBytes",
        "desc": "主题消息最大值，单位为 Byte，最大值为8388608Byte（即8MB）。"
      },
      {
        "name": "CleanUpPolicy",
        "desc": "消息删除策略，可以选择delete 或者compact"
      }
    ],
    "desc": "本接口用于修改主题属性。"
  },
  "CreateTopicIpWhiteList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "TopicName",
        "desc": "主题名称"
      },
      {
        "name": "IpWhiteList",
        "desc": "ip白名单列表"
      }
    ],
    "desc": "创建主题ip白名单"
  },
  "DescribeGroup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "SearchWord",
        "desc": "搜索关键字"
      },
      {
        "name": "Offset",
        "desc": "偏移量"
      },
      {
        "name": "Limit",
        "desc": "最大返回数量"
      }
    ],
    "desc": "枚举消费分组(精简版)"
  },
  "ModifyGroupOffsets": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "kafka实例id"
      },
      {
        "name": "Group",
        "desc": "kafka 消费分组"
      },
      {
        "name": "Strategy",
        "desc": "重置offset的策略，入参含义 0. 对齐shift-by参数，代表把offset向前或向后移动shift条 1. 对齐参考(by-duration,to-datetime,to-earliest,to-latest),代表把offset移动到指定timestamp的位置 2. 对齐参考(to-offset)，代表把offset移动到指定的offset位置"
      },
      {
        "name": "Topics",
        "desc": "表示需要重置的topics， 不填表示全部"
      },
      {
        "name": "Shift",
        "desc": "当strategy为0时，必须包含该字段，可以大于零代表会把offset向后移动shift条，小于零则将offset向前回溯shift条数。正确重置后新的offset应该是(old_offset + shift)，需要注意的是如果新的offset小于partition的earliest则会设置为earliest，如果大于partition 的latest则会设置为latest"
      },
      {
        "name": "ShiftTimestamp",
        "desc": "单位ms。当strategy为1时，必须包含该字段，其中-2表示重置offset到最开始的位置，-1表示重置到最新的位置(相当于清空)，其它值则代表指定的时间，会获取topic中指定时间的offset然后进行重置，需要注意的时，如果指定的时间不存在消息，则获取最末尾的offset。"
      },
      {
        "name": "Offset",
        "desc": "需要重新设置的offset位置。当strategy为2，必须包含该字段。"
      }
    ],
    "desc": "设置Groups 消费分组offset"
  },
  "DescribeInstances": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "（过滤条件）按照实例ID过滤"
      },
      {
        "name": "SearchWord",
        "desc": "（过滤条件）按照实例名称过滤，支持模糊查询"
      },
      {
        "name": "Status",
        "desc": "（过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部"
      },
      {
        "name": "Offset",
        "desc": "偏移量，不填默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认10，最大值100"
      },
      {
        "name": "TagKey",
        "desc": "匹配标签key值。"
      }
    ],
    "desc": "本接口（DescribeInstance）用于在用户账户下获取消息队列 CKafka 实例列表"
  },
  "ModifyInstanceAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id"
      },
      {
        "name": "MsgRetentionTime",
        "desc": "实例日志的最长保留时间，单位分钟，最大30天，0代表不开启日志保留时间回收策略"
      },
      {
        "name": "InstanceName",
        "desc": "实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)"
      },
      {
        "name": "Config",
        "desc": "实例配置"
      }
    ],
    "desc": "设置实例属性"
  },
  "DescribeUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "SearchWord",
        "desc": "按照名称过滤"
      },
      {
        "name": "Offset",
        "desc": "偏移"
      },
      {
        "name": "Limit",
        "desc": "本次返回个数"
      }
    ],
    "desc": "查询用户信息"
  },
  "DescribeACL": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "ResourceType",
        "desc": "Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "ResourceName",
        "desc": "资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称"
      },
      {
        "name": "Offset",
        "desc": "偏移位置"
      },
      {
        "name": "Limit",
        "desc": "个数限制"
      },
      {
        "name": "SearchWord",
        "desc": "关键字匹配"
      }
    ],
    "desc": "枚举ACL"
  },
  "DescribeTopicDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id"
      },
      {
        "name": "SearchWord",
        "desc": "（过滤条件）按照topicName过滤，支持模糊查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，不填默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认 10，最大值20，取值要大于0"
      }
    ],
    "desc": "获取主题列表详情（仅控制台调用）"
  },
  "CreateInstancePre": {
    "params": [
      {
        "name": "InstanceName",
        "desc": "实例名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)"
      },
      {
        "name": "ZoneId",
        "desc": "可用区"
      },
      {
        "name": "Period",
        "desc": "预付费购买时长，例如 \"1m\",就是一个月"
      },
      {
        "name": "InstanceType",
        "desc": "实例规格，1：入门型 ，2： 标准型，3 ：进阶型，4 ：容量型，5： 高阶型1，6：高阶性2, 7： 高阶型3,8： 高阶型4， 9 ：独占型。"
      },
      {
        "name": "VpcId",
        "desc": "vpcId，不填默认基础网络"
      },
      {
        "name": "SubnetId",
        "desc": "子网id，vpc网络需要传该参数，基础网络可以不传"
      },
      {
        "name": "MsgRetentionTime",
        "desc": "可选。实例日志的最长保留时间，单位分钟，默认为10080（7天），最大30天，不填默认0，代表不开启日志保留时间回收策略"
      },
      {
        "name": "ClusterId",
        "desc": "创建实例时可以选择集群Id, 该入参表示集群Id"
      },
      {
        "name": "RenewFlag",
        "desc": "预付费自动续费标记，0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费(用户设置)"
      }
    ],
    "desc": "创建实例(预付费包年包月)"
  },
  "DeleteTopicIpWhiteList": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例ID"
      },
      {
        "name": "TopicName",
        "desc": "主题名称"
      },
      {
        "name": "IpWhiteList",
        "desc": "ip白名单列表"
      }
    ],
    "desc": "删除主题IP白名单"
  },
  "ModifyPassword": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Name",
        "desc": "用户名称"
      },
      {
        "name": "Password",
        "desc": "用户当前密码"
      },
      {
        "name": "PasswordNew",
        "desc": "用户新密码"
      }
    ],
    "desc": "修改密码"
  },
  "DescribeConsumerGroup": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ckafka实例id。"
      },
      {
        "name": "GroupName",
        "desc": "可选，用户需要查询的group名称。"
      },
      {
        "name": "TopicName",
        "desc": "可选，用户需要查询的group中的对应的topic名称，如果指定了该参数，而group又未指定则忽略该参数。"
      },
      {
        "name": "Limit",
        "desc": "本次返回个数限制"
      },
      {
        "name": "Offset",
        "desc": "偏移位置"
      }
    ],
    "desc": "查询消费分组信息"
  },
  "CreateTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "TopicName",
        "desc": "主题名称，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)"
      },
      {
        "name": "PartitionNum",
        "desc": "Partition个数，大于0"
      },
      {
        "name": "ReplicaNum",
        "desc": "副本个数，不能多于 broker 数，最大为3"
      },
      {
        "name": "EnableWhiteList",
        "desc": "ip白名单开关, 1:打开  0:关闭，默认不打开"
      },
      {
        "name": "IpWhiteList",
        "desc": "Ip白名单列表，配额限制，enableWhileList=1时必选"
      },
      {
        "name": "CleanUpPolicy",
        "desc": "清理日志策略，日志清理模式，默认为\"delete\"。\"delete\"：日志按保存时间删除，\"compact\"：日志按 key 压缩，\"compact, delete\"：日志按 key 压缩且会按保存时间删除。"
      },
      {
        "name": "Note",
        "desc": "主题备注，是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)"
      },
      {
        "name": "MinInsyncReplicas",
        "desc": "默认为1"
      },
      {
        "name": "UncleanLeaderElectionEnable",
        "desc": "是否允许未同步的副本选为leader，false:不允许，true:允许，默认不允许"
      },
      {
        "name": "RetentionMs",
        "desc": "可消息选。保留时间，单位ms，当前最小值为60000ms"
      },
      {
        "name": "SegmentMs",
        "desc": "Segment分片滚动的时长，单位ms，当前最小为3600000ms"
      }
    ],
    "desc": "创建ckafka主题"
  },
  "CreatePartition": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "TopicName",
        "desc": "主题名称"
      },
      {
        "name": "PartitionNum",
        "desc": "主题分区个数"
      }
    ],
    "desc": "本接口用于增加主题中的分区"
  },
  "DeleteAcl": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id信息"
      },
      {
        "name": "ResourceType",
        "desc": "Acl资源类型，(0:UNKNOWN，1:ANY，2:TOPIC，3:GROUP，4:CLUSTER，5:TRANSACTIONAL_ID)，当前只有TOPIC，其它字段用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "ResourceName",
        "desc": "资源名称，和resourceType相关，如当resourceType为TOPIC时，则该字段表示topic名称，当resourceType为GROUP时，该字段表示group名称"
      },
      {
        "name": "Operation",
        "desc": "Acl操作方式，(0:UNKNOWN，1:ANY，2:ALL，3:READ，4:WRITE，5:CREATE，6:DELETE，7:ALTER，8:DESCRIBE，9:CLUSTER_ACTION，10:DESCRIBE_CONFIGS，11:ALTER_CONFIGS，12:IDEMPOTEN_WRITE)，当前ckafka只支持READ,WRITE，其它用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "PermissionType",
        "desc": "权限类型，(0:UNKNOWN，1:ANY，2:DENY，3:ALLOW)，当前ckakfa支持ALLOW(相当于白名单)，其它用于后续兼容开源kafka的acl时使用"
      },
      {
        "name": "Host",
        "desc": "默认为\\*，表示任何host都可以访问，当前ckafka不支持host为\\*，但是后面开源kafka的产品化会直接支持"
      },
      {
        "name": "Principal",
        "desc": "用户列表，默认为*，表示任何user都可以访问，当前用户只能是用户列表中包含的用户"
      }
    ],
    "desc": "删除ACL"
  },
  "DescribeAppInfo": {
    "params": [
      {
        "name": "Offset",
        "desc": "偏移位置"
      },
      {
        "name": "Limit",
        "desc": "本次查询用户数目最大数量限制，最大值为50，默认50"
      }
    ],
    "desc": "查询用户列表"
  },
  "DescribeGroupOffsets": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "（过滤条件）按照实例 ID 过滤"
      },
      {
        "name": "Group",
        "desc": "Kafka 消费分组"
      },
      {
        "name": "Topics",
        "desc": "group 订阅的主题名称数组，如果没有该数组，则表示指定的 group 下所有 topic 信息"
      },
      {
        "name": "SearchWord",
        "desc": "模糊匹配 topicName"
      },
      {
        "name": "Offset",
        "desc": "本次查询的偏移位置，默认为0"
      },
      {
        "name": "Limit",
        "desc": "本次返回结果的最大个数，默认为50，最大值为50"
      }
    ],
    "desc": "获取消费分组offset"
  },
  "DescribeInstanceAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例id"
      }
    ],
    "desc": "获取实例属性"
  },
  "DescribeInstancesDetail": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "（过滤条件）按照实例ID过滤"
      },
      {
        "name": "SearchWord",
        "desc": "（过滤条件）按照实例名称过滤，支持模糊查询"
      },
      {
        "name": "Status",
        "desc": "（过滤条件）实例的状态。0：创建中，1：运行中，2：删除中，不填默认返回全部"
      },
      {
        "name": "Offset",
        "desc": "偏移量，不填默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认10，最大值20"
      },
      {
        "name": "TagKey",
        "desc": "匹配标签key值。"
      },
      {
        "name": "Filters",
        "desc": "过滤器"
      }
    ],
    "desc": "用户账户下获取实例列表详情"
  },
  "DeleteUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Name",
        "desc": "用户名称"
      }
    ],
    "desc": "删除用户"
  },
  "DescribeTopicAttributes": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID"
      },
      {
        "name": "TopicName",
        "desc": "主题名称"
      }
    ],
    "desc": "获取主题属性\n"
  },
  "DescribeTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例 ID"
      },
      {
        "name": "SearchWord",
        "desc": "过滤条件，按照 topicName 过滤，支持模糊查询"
      },
      {
        "name": "Offset",
        "desc": "偏移量，不填默认为0"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认为10，最大值为50"
      }
    ],
    "desc": "接口请求域名：https://ckafka.tencentcloudapi.com\n本接口（DescribeTopic）用于在用户获取消息队列 CKafka 实例的主题列表"
  },
  "CreateUser": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "实例Id"
      },
      {
        "name": "Name",
        "desc": "用户名称"
      },
      {
        "name": "Password",
        "desc": "用户密码"
      }
    ],
    "desc": "添加用户"
  },
  "DeleteTopic": {
    "params": [
      {
        "name": "InstanceId",
        "desc": "ckafka 实例Id"
      },
      {
        "name": "TopicName",
        "desc": "ckafka 主题名称"
      }
    ],
    "desc": "删除ckafka主题"
  }
}