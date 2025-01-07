**Example 1: 查询该租户**



Input: 

```
tccli tdmq GetTopicList --cli-unfold-argument  \
    --EnvironmentId devNs \
    --Offset 1 \
    --Limit 1 \
    --ClusterId pulsar-uahenidn
```

Output: 
```
{
    "Response": {
        "RequestId": "4854c6de-732f-4b8f-b23b-1081f3bf3bc3",
        "TopicList": [
            {
                "TopicName": "1733317358581",
                "PulsarTopicType": 3
            }
        ],
        "TotalCount": 1
    }
}
```

