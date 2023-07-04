**Example 1: 修改Kafka导入配置**

修改Kafka导入配置

Input: 

```
tccli cls ModifyKafkaRecharge --cli-unfold-argument  \
    --Id xxx-xxx-xx \
    --TopicId abc \
    --Name abc \
    --ServerAddr abc \
    --IsEncryptionAddr True \
    --UserKafkaTopics abc \
    --ConsumerGroupName abc \
    --LogRechargeRule.RechargeType json_log \
    --LogRechargeRule.TimeKey abc \
    --LogRechargeRule.TimeFormat abc \
    --LogRechargeRule.LogRegex abc \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.DefaultTimeSwitch True \
    --LogRechargeRule.UnMatchLogKey abc \
    --LogRechargeRule.EncodingFormat 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

