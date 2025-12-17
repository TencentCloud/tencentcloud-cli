**Example 1: 获取日志主题详情**



Input: 

```
tccli cls GetTopicDetail --cli-unfold-argument  \
    --TopicId 67c85f5f-57a0-433c-9176-109ad0d5496e
```

Output: 
```
{
    "Response": {
        "TopicInfo": {
            "AssumerName": "",
            "AssumerUin": 0,
            "AutoSplit": true,
            "BizType": 0,
            "CreateTime": "2025-04-18 10:45:14",
            "Describes": "",
            "EffectiveDate": "",
            "Extends": {
                "AnonymousAccess": null
            },
            "HotPeriod": 0,
            "Index": false,
            "IsWebTracking": false,
            "KeyId": "",
            "LogsetId": "0af7e6bb-fc91-4ee8-ad24-1129e9c91c6c",
            "MaxSplitPartitions": 300,
            "MigrationStatus": 0,
            "PartitionCount": 1,
            "Period": 30,
            "RoleName": "",
            "Status": true,
            "StorageType": "hot",
            "SubAssumerName": "",
            "Tags": [
                {
                    "Key": "bowww***est1",
                    "Value": "bowww***alue1"
                }
            ],
            "TopicAsyncTaskID": "",
            "TopicId": "67c85f5f-57a0-433c-9176-109ad0d5496e",
            "TopicName": "bowwwang***iod-hot"
        },
        "RequestId": "1085ad97-2560-44fa-bfaf-ead7d831d62e"
    }
}
```

