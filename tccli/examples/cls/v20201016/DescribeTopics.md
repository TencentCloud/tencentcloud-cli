**Example 1: 获取日志主题列表**

获取日志主题列表

Input: 

```
tccli cls DescribeTopics --cli-unfold-argument  \
    --Offset 10 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Topics": [
            {
                "Index": true,
                "PartitionCount": 1,
                "Describes": "x1",
                "Status": true,
                "Tags": [
                    {
                        "Value": "x10",
                        "Key": "x11"
                    }
                ],
                "AssumerName": "x12",
                "SubAssumerName": "x13",
                "MaxSplitPartitions": 0,
                "LogsetId": "x15",
                "TopicId": "x16",
                "HotPeriod": 1,
                "StorageType": "x17",
                "Period": 0,
                "AutoSplit": true,
                "CreateTime": "x18",
                "TopicName": "x19"
            }
        ],
        "RequestId": "x20"
    }
}
```

