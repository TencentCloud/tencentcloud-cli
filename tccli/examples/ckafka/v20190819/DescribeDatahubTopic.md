**Example 1: 获取主题属性**



Input: 

```
tccli ckafka DescribeDatahubTopic --cli-unfold-argument  \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "UserName": "xx",
            "TopicId": "xx",
            "Name": "xx",
            "PartitionNum": 1,
            "Status": 1,
            "Note": "xx",
            "RetentionMs": 1,
            "Password": "xx",
            "TopicName": "xx"
        },
        "RequestId": "xx"
    }
}
```

