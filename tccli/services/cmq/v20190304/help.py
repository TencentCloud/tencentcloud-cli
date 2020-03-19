# -*- coding: utf-8 -*-
DESC = "cmq-2019-03-04"
INFO = {
  "CreateTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "MaxMsgSize",
        "desc": "MaxMsgSize"
      },
      {
        "name": "FilterType",
        "desc": "FilterType"
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "MsgRetentionSeconds"
      },
      {
        "name": "Trace",
        "desc": "是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。"
      }
    ],
    "desc": "创建主题"
  },
  "CreateSubscribe": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "SubscriptionName",
        "desc": "SubscriptionName"
      },
      {
        "name": "Protocol",
        "desc": "Protocol"
      },
      {
        "name": "Endpoint",
        "desc": "Endpoint"
      },
      {
        "name": "NotifyStrategy",
        "desc": "NotifyStrategy"
      },
      {
        "name": "FilterTag",
        "desc": "FilterTag"
      },
      {
        "name": "BindingKey",
        "desc": "BindingKey"
      },
      {
        "name": "NotifyContentFormat",
        "desc": "NotifyContentFormat"
      }
    ],
    "desc": "创建订阅接口"
  },
  "ModifyTopicAttribute": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "MaxMsgSize",
        "desc": "MaxMsgSize"
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "MsgRetentionSeconds"
      },
      {
        "name": "Trace",
        "desc": "是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。"
      }
    ],
    "desc": "修改主题属性"
  },
  "ClearSubscriptionFilterTags": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "SubscriptionName",
        "desc": "SubscriptionName"
      }
    ],
    "desc": "清空订阅者消息标签"
  },
  "DeleteSubscribe": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "SubscriptionName",
        "desc": "SubscriptionName"
      }
    ],
    "desc": "删除订阅"
  },
  "CreateQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "队列名字，在单个地域同一帐号下唯一。队列名称是一个不超过 64 个字符的字符串，必须以字母为首字符，剩余部分可以包含字母、数字和横划线(-)。"
      },
      {
        "name": "MaxMsgHeapNum",
        "desc": "最大堆积消息数。取值范围在公测期间为 1,000,000 - 10,000,000，正式上线后范围可达到 1000,000-1000,000,000。默认取值在公测期间为 10,000,000，正式上线后为 100,000,000。"
      },
      {
        "name": "PollingWaitSeconds",
        "desc": "消息接收长轮询等待时间。取值范围 0-30 秒，默认值 0。"
      },
      {
        "name": "VisibilityTimeout",
        "desc": "消息可见性超时。取值范围 1-43200 秒（即12小时内），默认值 30。"
      },
      {
        "name": "MaxMsgSize",
        "desc": "消息最大长度。取值范围 1024-65536 Byte（即1-64K），默认值 65536。"
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "消息保留周期。取值范围 60-1296000 秒（1min-15天），默认值 345600 (4 天)。"
      },
      {
        "name": "RewindSeconds",
        "desc": "队列是否开启回溯消息能力，该参数取值范围0-msgRetentionSeconds,即最大的回溯时间为消息在队列中的保留周期，0表示不开启。"
      },
      {
        "name": "Transaction",
        "desc": "1 表示事务队列，0 表示普通队列"
      },
      {
        "name": "FirstQueryInterval",
        "desc": "第一次回查间隔"
      },
      {
        "name": "MaxQueryCount",
        "desc": "最大回查次数"
      },
      {
        "name": "DeadLetterQueueName",
        "desc": "死信队列名称"
      },
      {
        "name": "Policy",
        "desc": "死信策略。0为消息被多次消费未删除，1为Time-To-Live过期"
      },
      {
        "name": "MaxReceiveCount",
        "desc": "最大接收次数 1-1000"
      },
      {
        "name": "MaxTimeToLive",
        "desc": "policy为1时必选。最大未消费过期时间。范围300-43200，单位秒，需要小于消息最大保留时间msgRetentionSeconds"
      },
      {
        "name": "Trace",
        "desc": "是否开启消息轨迹追踪，当不设置字段时，默认为不开启，该字段为true表示开启，为false表示不开启"
      }
    ],
    "desc": "创建队列接口\n"
  },
  "RewindQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "QueueName"
      },
      {
        "name": "StartConsumeTime",
        "desc": "设定该时间，则（Batch）receiveMessage接口，会按照生产消息的先后顺序消费该时间戳以后的消息。"
      }
    ],
    "desc": "回溯队列"
  },
  "ModifySubscriptionAttribute": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "SubscriptionName",
        "desc": "SubscriptionName"
      },
      {
        "name": "NotifyStrategy",
        "desc": "NotifyStrategy"
      },
      {
        "name": "NotifyContentFormat",
        "desc": "NotifyContentFormat"
      },
      {
        "name": "FilterTags",
        "desc": "FilterTags"
      },
      {
        "name": "BindingKey",
        "desc": "BindingKey"
      }
    ],
    "desc": "修改订阅属性"
  },
  "DescribeQueueDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页时本页获取队列列表的起始位置。如果填写了该值，必须也要填写 limit 。该值缺省时，后台取默认值 0"
      },
      {
        "name": "Limit",
        "desc": "分页时本页获取队列的个数，如果不传递该参数，则该参数默认为20，最大值为50。"
      },
      {
        "name": "Filters",
        "desc": "筛选参数，目前支持QueueName筛选，且仅支持一个关键字"
      },
      {
        "name": "TagKey",
        "desc": "标签搜索"
      },
      {
        "name": "QueueName",
        "desc": "精确匹配QueueName"
      }
    ],
    "desc": "枚举队列"
  },
  "DeleteQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "队列名称"
      }
    ],
    "desc": "DeleteQueue"
  },
  "UnbindDeadLetter": {
    "params": [
      {
        "name": "QueueName",
        "desc": "死信策略源队列名称，调用本接口会清空该队列的死信队列策略。"
      }
    ],
    "desc": "解绑死信队列"
  },
  "DeleteTopic": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      }
    ],
    "desc": "删除主题"
  },
  "DescribeTopicDetail": {
    "params": [
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      },
      {
        "name": "Filters",
        "desc": "目前只支持过滤TopicName ， 且只能填一个过滤值"
      },
      {
        "name": "TagKey",
        "desc": "TagKey"
      },
      {
        "name": "TopicName",
        "desc": "精确匹配TopicName"
      }
    ],
    "desc": "查询主题详情"
  },
  "DescribeSubscriptionDetail": {
    "params": [
      {
        "name": "TopicName",
        "desc": "TopicName"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Limit"
      },
      {
        "name": "Filters",
        "desc": "目前只支持SubscriptionName，且仅支持一个关键字"
      }
    ],
    "desc": "查询订阅详情"
  },
  "DescribeDeadLetterSourceQueues": {
    "params": [
      {
        "name": "DeadLetterQueueName",
        "desc": "死信队列名称"
      },
      {
        "name": "Limit",
        "desc": "limit"
      },
      {
        "name": "Offset",
        "desc": "offset"
      },
      {
        "name": "Filters",
        "desc": "过滤死信队列源队列名称，目前仅支持SourceQueueName过滤"
      }
    ],
    "desc": "枚举死信队列源队列"
  },
  "ClearQueue": {
    "params": [
      {
        "name": "QueueName",
        "desc": "队列名称"
      }
    ],
    "desc": "清除queue中的所有消息"
  },
  "ModifyQueueAttribute": {
    "params": [
      {
        "name": "QueueName",
        "desc": "QueueName"
      },
      {
        "name": "MaxMsgHeapNum",
        "desc": "MaxMsgHeapNum"
      },
      {
        "name": "PollingWaitSeconds",
        "desc": "PollingWaitSeconds"
      },
      {
        "name": "VisibilityTimeout",
        "desc": "VisibilityTimeout"
      },
      {
        "name": "MaxMsgSize",
        "desc": "MaxMsgSize"
      },
      {
        "name": "MsgRetentionSeconds",
        "desc": "MsgRetentionSeconds"
      },
      {
        "name": "RewindSeconds",
        "desc": "RewindSeconds"
      },
      {
        "name": "FirstQueryInterval",
        "desc": "FirstQueryInterval"
      },
      {
        "name": "MaxQueryCount",
        "desc": "MaxQueryCount"
      },
      {
        "name": "DeadLetterQueueName",
        "desc": "DeadLetterQueueName"
      },
      {
        "name": "MaxTimeToLive",
        "desc": "MaxTimeToLive"
      },
      {
        "name": "MaxReceiveCount",
        "desc": "MaxReceiveCount"
      },
      {
        "name": "Policy",
        "desc": "Policy"
      },
      {
        "name": "Trace",
        "desc": "是否开启消息轨迹标识，true表示开启，false表示不开启，不填表示不开启。"
      }
    ],
    "desc": "修改队列属性"
  }
}