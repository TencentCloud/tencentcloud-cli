**Example 1: 查询Datahub主题列表**



Input: 

```
tccli ckafka DescribeDatahubTopics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "TopicList": [
                {
                    "Name": "abc",
                    "TopicName": "abc",
                    "TopicId": "abc",
                    "PartitionNum": 1,
                    "RetentionMs": 1,
                    "Note": "abc",
                    "Status": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

