**Example 1: 创建Kafka导入规则**

创建Kafka导入规则

Input: 

```
tccli cls CreateKafkaRecharge --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx-xxxx \
    --Name test \
    --KafkaType 1 \
    --ServerAddr abc \
    --IsEncryptionAddr True \
    --UserKafkaTopics abc \
    --ConsumerGroupName abc \
    --Offset -1 \
    --LogRechargeRule.RechargeType json_log \
    --LogRechargeRule.TimeKey abc \
    --LogRechargeRule.TimeFormat abc \
    --LogRechargeRule.LogRegex abc \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.UnMatchLogKey abc \
    --LogRechargeRule.DefaultTimeSwitch True \
    --LogRechargeRule.EncodingFormat 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Id": "xxx-xx-xx"
    }
}
```

