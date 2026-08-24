**Example 1: DescribeCkafkaTopicList**



Input: 

```
tccli csip DescribeDspmCkafkaTopicList --cli-unfold-argument  \
    --VipType 0 \
    --RegionId vpc-sads32we \
    --InstanceId ins-2ws43refg \
    --InstanceName ins-21wsd5r
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "TopicId": "topic-wqsa",
                "TopicName": "sender_alarm"
            }
        ],
        "TotalCount": 0,
        "RequestId": "013dced9-2c45-472f-9b28-862666348d0d"
    }
}
```

