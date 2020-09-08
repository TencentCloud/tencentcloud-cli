# -*- coding: utf-8 -*-
DESC = "tdmq-2020-02-17"
INFO = {
  "CreateTopic": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名，不支持中字以及除了短线和下划线外的特殊字符且不超过32个字符。"
      },
      {
        "name": "Partitions",
        "desc": "0：非分区topic，无分区；非0：具体分区topic的分区数，最大不允许超过128。"
      },
      {
        "name": "TopicType",
        "desc": "0： 普通消息；\n1 ：全局顺序消息；\n2 ：局部顺序消息；\n3 ：重试队列；\n4 ：死信队列；\n5 ：事务消息。"
      },
      {
        "name": "Remark",
        "desc": "备注，128字符以内。"
      }
    ],
    "desc": "新增指定分区、类型的消息主题"
  },
  "DeleteEnvironments": {
    "params": [
      {
        "name": "EnvironmentIds",
        "desc": "环境（命名空间）数组，每次最多删除20个。"
      }
    ],
    "desc": "批量删除租户下的环境"
  },
  "DescribeEnvironments": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称，模糊搜索。"
      },
      {
        "name": "Offset",
        "desc": "起始下标，不填默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认为10，最大值为20。"
      }
    ],
    "desc": "获取租户下环境列表"
  },
  "ModifyTopic": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名。"
      },
      {
        "name": "Partitions",
        "desc": "分区数，必须大于或者等于原分区数，若想维持原分区数请输入原数目，修改分区数仅对非全局顺序消息起效果，不允许超过128个分区。"
      },
      {
        "name": "Remark",
        "desc": "备注，128字符以内。"
      }
    ],
    "desc": "修改主题备注和分区数"
  },
  "DeleteTopics": {
    "params": [
      {
        "name": "TopicSets",
        "desc": "主题集合，每次最多删除20个。"
      }
    ],
    "desc": "批量删除topics"
  },
  "CreateSubscription": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名称。"
      },
      {
        "name": "SubscriptionName",
        "desc": "订阅者名称，不支持中字以及除了短线和下划线外的特殊字符且不超过150个字符。"
      },
      {
        "name": "IsIdempotent",
        "desc": "是否幂等创建，若否不允许创建同名的订阅关系。"
      },
      {
        "name": "Remark",
        "desc": "备注，128个字符以内。"
      }
    ],
    "desc": "创建一个主题的订阅关系"
  },
  "DescribeSubscriptions": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名称。"
      },
      {
        "name": "Offset",
        "desc": "起始下标，不填默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认为10，最大值为20。"
      },
      {
        "name": "SubscriptionName",
        "desc": "订阅者名称，模糊匹配。"
      },
      {
        "name": "Filters",
        "desc": "数据过滤条件。"
      }
    ],
    "desc": "查询指定环境和主题下的订阅者列表"
  },
  "DescribeEnvironmentAttributes": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      }
    ],
    "desc": "获取指定环境的属性"
  },
  "CreateEnvironment": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称，不支持中字以及除了短线和下划线外的特殊字符且不超过16个字符。"
      },
      {
        "name": "MsgTTL",
        "desc": "未消费消息过期时间，单位：秒，最小60，最大1296000，（15天）。"
      },
      {
        "name": "Remark",
        "desc": "说明，128个字符以内。"
      }
    ],
    "desc": "用于在用户账户下创建消息队列 Tdmq环境（命名空间）"
  },
  "ModifyEnvironmentAttributes": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "MsgTTL",
        "desc": "未消费消息过期时间，单位：秒，最大1296000。"
      },
      {
        "name": "Remark",
        "desc": "备注，字符串最长不超过128。"
      }
    ],
    "desc": "修改指定环境的属性值"
  },
  "ResetMsgSubOffsetByTimestamp": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名称。"
      },
      {
        "name": "Subscription",
        "desc": "订阅者名称。"
      },
      {
        "name": "ToTimestamp",
        "desc": "时间戳，精确到毫秒。"
      }
    ],
    "desc": "根据时间戳进行消息回溯，精确到毫秒"
  },
  "DescribeProducers": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名。"
      },
      {
        "name": "Offset",
        "desc": "起始下标，不填默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认为10，最大值为20。"
      },
      {
        "name": "ProducerName",
        "desc": "生产者名称，模糊匹配。"
      }
    ],
    "desc": "获取生产者列表，仅显示在线的生产者"
  },
  "DescribeTopics": {
    "params": [
      {
        "name": "EnvironmentId",
        "desc": "环境（命名空间）名称。"
      },
      {
        "name": "TopicName",
        "desc": "主题名模糊匹配。"
      },
      {
        "name": "Offset",
        "desc": "起始下标，不填默认为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，不填则默认为10，最大值为20。"
      },
      {
        "name": "TopicType",
        "desc": "topic类型描述：\n0：普通消息；\n1：全局顺序消息；\n2：局部顺序消息；\n3：重试队列；\n4：死信队列；\n5：事务消息。"
      }
    ],
    "desc": "获取环境下主题列表"
  },
  "DeleteSubscriptions": {
    "params": [
      {
        "name": "SubscriptionTopicSets",
        "desc": "订阅关系集合，每次最多删除20个。"
      }
    ],
    "desc": "删除订阅关系"
  }
}