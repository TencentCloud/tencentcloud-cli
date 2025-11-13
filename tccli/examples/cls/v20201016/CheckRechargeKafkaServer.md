**Example 1: 校验用户输入Kafka服务地址是否可访问**

校验用户输入Kafka服务地址是否可访问

Input: 

```
tccli cls CheckRechargeKafkaServer --cli-unfold-argument  \
    --KafkaType 0 \
    --KafkaInstance ckafka-8j4ro59xx \
    --UserKafkaMeta.KafkaVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "add346ce-36c5-4961-917f-c020b5fc4bfd"
    }
}
```

