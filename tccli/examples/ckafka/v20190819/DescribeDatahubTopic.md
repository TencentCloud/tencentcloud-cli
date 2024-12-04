**Example 1: 获取主题属性**



Input: 

```
tccli ckafka DescribeDatahubTopic --cli-unfold-argument  \
    --Name 1300957330-tanxing-qiang-2nd
```

Output: 
```
{
    "Response": {
        "RequestId": "e4edf3bd-b2b1-4add-9a87-d41f35091395",
        "Result": {
            "Address": "dip.tencentcloudmq.com:6000",
            "Name": "1300957330-tanxing-qiang-2nd",
            "Note": "",
            "PartitionNum": 1,
            "Password": "923274dd1f22496590f7ff598d773895",
            "RetentionMs": 86400000,
            "Status": 1,
            "TopicId": "topic-g1ntq6se",
            "TopicName": "1300957330-tanxing-qiang-2nd",
            "UserName": "ougeml7y4ky0"
        }
    }
}
```

