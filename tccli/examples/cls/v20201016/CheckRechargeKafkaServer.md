**Example 1: 校验用户输入Kafka服务地址是否可访问**

校验用户输入Kafka服务地址是否可访问

Input: 

```
tccli cls CheckRechargeKafkaServer --cli-unfold-argument  \
    --KafkaType 1 \
    --ServerAddr est.cls.tencentyun.com:9095 \
    --IsEncryptionAddr False
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx",
        "Status": 0
    }
}
```

