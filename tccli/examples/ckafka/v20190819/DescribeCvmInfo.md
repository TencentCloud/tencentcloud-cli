**Example 1: 获取实例CVM信息示例**



Input: 

```
tccli ckafka DescribeCvmInfo --cli-unfold-argument  \
    --InstanceId ckafka-6er88krk
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "CvmList": [
                {
                    "CkafkaInstanceId": "ckafka-6er88krk",
                    "InstanceId": "ins-axxxas",
                    "Ip": "10.0.0.23"
                }
            ]
        },
        "RequestId": "31740399-5d06-404b-a4b5-3652e21c8a1d"
    }
}
```

