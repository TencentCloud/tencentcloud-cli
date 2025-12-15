**Example 1: 获取日志主题列表**

获取日志主题列表

Input: 

```
tccli cls DescribeTopics --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "9402a324-xxxx-xxxx-xxxx-2bc613cd187e",
        "Topics": [
            {
                "AssumerName": "",
                "AssumerUin": 0,
                "AutoSplit": true,
                "BizType": 0,
                "CreateTime": "2024-12-26 19:28:55",
                "Describes": "",
                "EffectiveDate": "",
                "Extends": {
                    "AnonymousAccess": null
                },
                "HotPeriod": 0,
                "Index": true,
                "IsWebTracking": false,
                "LogsetId": "fd0605ca-xxxx-xxxx-xxxx-592e5233c2db",
                "MaxSplitPartitions": 50,
                "MigrationStatus": 0,
                "PartitionCount": 1,
                "Period": 1,
                "RoleName": "",
                "Status": true,
                "StorageType": "hot",
                "SubAssumerName": "",
                "Tags": [],
                "TopicAsyncTaskID": "",
                "TopicId": "8a41c585-xxxx-xxxx-xxxx-c358a595f662",
                "TopicName": "topic-name-test"
            }
        ],
        "TotalCount": 1544
    }
}
```

