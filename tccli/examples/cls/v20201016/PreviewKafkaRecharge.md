**Example 1: Kafka导入数据预览**

源数据预览

Input: 

```
tccli cls PreviewKafkaRecharge --cli-unfold-argument  \
    --PreviewType 1 \
    --KafkaType 0 \
    --KafkaInstance ckafka-k9m5vj75 \
    --UserKafkaTopics topic_111b1f24-1ce6-45a3-a515-6e293429f111,topic_11161155-0ea3-4e53-9626-72b4837a4111,topic_111f125e-86f6-41c9-9dcc-360594290111 \
    --ConsumerGroupName  \
    --Offset -1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx",
        "LogData": "rmap[AvailIndexTraffic:0 AvailStore:0 ClusterAvailableTrafficCapacity:0...",
        "LogSample": ""
    }
}
```

**Example 2: Kafaka导入数据预览**

导出结果预览

Input: 

```
tccli cls PreviewKafkaRecharge --cli-unfold-argument  \
    --PreviewType 2 \
    --KafkaType 0 \
    --KafkaInstance ckafka-l4rped7z \
    --UserKafkaTopics topic_111b1f24-1ce6-45a3-a515-6e293429f111,topic_11161155-0ea3-4e53-9626-72b4837a4111,topic_111f125e-86f6-41c9-9dcc-360594290111 \
    --ConsumerGroupName  \
    --Offset -2 \
    --LogRechargeRule.RechargeType minimalist_log \
    --LogRechargeRule.LogRegex  \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.UnMatchLogKey LogParseFailure \
    --LogRechargeRule.UnMatchLogTimeSrc 0 \
    --LogRechargeRule.EncodingFormat 0 \
    --LogRechargeRule.DefaultTimeSwitch True \
    --LogRechargeRule.DefaultTimeSrc 0 \
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
        "LogSample": "{\"x-intranet-proxy-region\":\"sh\",\"x-intranet-proxy-socket-local-address\":\"::ffff:11.179.111.111\",\"x-intranet-proxy-socket-local-port\":\"8443\"",
        "LogData": "{\"__CONTENT__\":\"{\\\"x-intranet-proxy-region\\\":\\\"sh\\\",\\\"x-intranet-proxy-socket-local-address\\\":\\\"::ffff:11.179.111.111\\\",\\\"x-intranet-proxy-socket-local-port\\\":\\\"8443\\\"",
        "RequestId": "d3218ba6-4d98-480a-a97b-8db0ae87ef31"
    }
}
```

