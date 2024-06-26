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
            "Name": "abc",
            "TopicName": "abc",
            "TopicId": "abc",
            "PartitionNum": 1,
            "RetentionMs": 1,
            "Note": "abc",
            "UserName": "abc",
            "Password": "abc",
            "Status": 1,
            "Address": "abc"
        },
        "RequestId": "abc"
    }
}
```

