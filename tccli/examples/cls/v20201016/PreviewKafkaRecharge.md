**Example 1: Kafka导入数据预览**

Kafka导入数据预览

Input: 

```
tccli cls PreviewKafkaRecharge --cli-unfold-argument  \
    --PreviewType 1 \
    --KafkaType 1 \
    --ServerAddr test.cls.tencentyun.com:9095 \
    --IsEncryptionAddr False \
    --UserKafkaTopics topic1,topic2 \
    --Offset 0 \
    --LogRechargeRule.RechargeType json_log \
    --LogRechargeRule.TimeKey abc \
    --LogRechargeRule.TimeFormat abc \
    --LogRechargeRule.LogRegex abc \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.UnMatchLogKey abc \
    --LogRechargeRule.EncodingFormat 0 \
    --LogRechargeRule.DefaultTimeSwitch True
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx",
        "LogData": "xxxxxxx",
        "LogSample": "abc"
    }
}
```

