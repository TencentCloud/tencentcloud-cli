**Example 1: 修改Kafka导入配置**

修改Kafka导入配置

Input: 

```
tccli cls ModifyKafkaRecharge --cli-unfold-argument  \
    --Id 1014cc79-f006-48e4-8820-1dc7270540c0 \
    --TopicId 06bdb6f6-ae6e-41f6-9e7b-fcab91cb0111 \
    --KafkaType 0 \
    --KafkaInstance ckafka-2vrgxbxa \
    --ServerAddr  \
    --IsEncryptionAddr False \
    --Protocol.Protocol  \
    --Protocol.Mechanism  \
    --Protocol.UserName  \
    --Protocol.Password  \
    --UserKafkaTopics topic-subs-0px4qkvu32-cdb-5zi7jf11 \
    --ConsumerGroupName  \
    --LogRechargeRule.RechargeType json_log \
    --LogRechargeRule.LogRegex  \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.UnMatchLogKey LogParseFailure \
    --LogRechargeRule.UnMatchLogTimeSrc 0 \
    --LogRechargeRule.EncodingFormat 0 \
    --LogRechargeRule.DefaultTimeSwitch True \
    --LogRechargeRule.DefaultTimeSrc 1 \
    --LogRechargeRule.TimeKey  \
    --LogRechargeRule.TimeRegex  \
    --LogRechargeRule.TimeFormat  \
    --LogRechargeRule.TimeZone UTC+08:00 \
    --LogRechargeRule.Metadata kafka_topic kafka_partition kafka_offset kafka_timestamp
```

Output: 
```
{
    "Response": {
        "RequestId": "0813f2a8-666f-47d4-886b-bf63bdcbc8d3"
    }
}
```

