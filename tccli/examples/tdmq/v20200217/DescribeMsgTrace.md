**Example 1: 获取消息轨迹**



Input: 

```
tccli tdmq DescribeMsgTrace --cli-unfold-argument  \
    --EnvironmentId default \
    --MsgId 16839:8:-1 \
    --ProduceTime 2020-08-1908:06:19
```

Output: 
```
{
    "Response": {
        "ProducerLog": {
            "MsgId": "16839:8:-1",
            "ProducerName": "fisrtProducer",
            "ProduceTime": "2020-08-19 08:06:19,211",
            "ProducerAddr": "9.139.220.17:57234",
            "ProduceUseTime": 5309,
            "Status": "success"
        },
        "ServerLog": {
            "SaveTime": "2020-08-19 08:06:19,211",
            "Status": "success"
        },
        "ConsumerLogs": {
            "TotalCount": 1,
            "ConsumerLogSets": [
                {
                    "MsgId": "16839:8:-1",
                    "ConsumerGroup": "sun_consumer",
                    "ConsumerName": "7ef60",
                    "ConsumeTime": "2020-08-19 08:06:22,563",
                    "ConsumerAddr": "9.139.220.17:57241",
                    "ConsumeUseTime": 875,
                    "Status": "success"
                }
            ]
        },
        "RequestId": "msgs"
    }
}
```

