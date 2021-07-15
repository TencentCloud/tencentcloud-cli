**Example 1: 获取日志主题列表**



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
                "Status": true,
                "TopicId": "xx",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "StorageType": "xx",
                "PartitionCount": 1,
                "MaxSplitPartitions": 0,
                "Period": 0,
                "AutoSplit": true,
                "LogsetId": "xx",
                "Index": true,
                "CreateTime": "xx",
                "TopicName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

