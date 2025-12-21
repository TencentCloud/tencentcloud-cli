**Example 1: 查询实例版本信息**

查询实例版本信息

Input: 

```
tccli ckafka DescribeCkafkaVersion --cli-unfold-argument  \
    --InstanceId ckafka-bqwlyrg8
```

Output: 
```
{
    "Response": {
        "Result": {
            "LatestBrokerVersion": [
                {
                    "KafkaVersion": "0.10.2",
                    "BrokerVersion": "v0.10.2.1_r1.2.11"
                },
                {
                    "KafkaVersion": "3.2.3",
                    "BrokerVersion": "v3.2.3_r1.0.7"
                },
                {
                    "KafkaVersion": "2.8.1",
                    "BrokerVersion": "v2.8.1_r1.1.6"
                },
                {
                    "KafkaVersion": "2.4.1",
                    "BrokerVersion": "v2.4.2_r1.2.4"
                },
                {
                    "KafkaVersion": "1.1.1",
                    "BrokerVersion": "v1.1.1_r1.1.14"
                }
            ],
            "KafkaVersion": "1.1.1",
            "CurBrokerVersion": "1.1.1_1.0.9"
        },
        "RequestId": "d173b4fb-c6d0-4507-a822-b6f277fc4016"
    }
}
```

