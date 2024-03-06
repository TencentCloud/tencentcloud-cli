**Example 1: 创建Kafka导入规则**

创建Kafka导入规则

Input: 

```
tccli cls CreateKafkaRecharge --cli-unfold-argument  \
    --TopicId b53fe5be-7ee3-4031-8043-5a73bad4f572 \
    --Name testname \
    --KafkaType 1 \
    --ServerAddr 192.168.0.1:9095 \
    --IsEncryptionAddr True \
    --UserKafkaTopics topic-1212123123,topic-sadf5r32f3ww \
    --ConsumerGroupName consumer-group-name \
    --Offset -1 \
    --LogRechargeRule.DefaultTimeSrc 0 \
    --LogRechargeRule.DefaultTimeSwitch True \
    --LogRechargeRule.EncodingFormat 0 \
    --LogRechargeRule.RechargeType minimalist_log \
    --LogRechargeRule.UnMatchLogKey LogParseFailure \
    --LogRechargeRule.UnMatchLogSwitch True \
    --LogRechargeRule.UnMatchLogTimeSrc 0 \
    --Protocol.Protocol plaintext
```

Output: 
```
{
    "Response": {
        "RequestId": "48d6a72b-99f7-4643-bc57-d63b6952b752",
        "Id": "11d6a72b-99f7-4643-bc57-d63b6952b711"
    }
}
```

