**Example 1: 获取日志主题列表**

获取日志主题列表

Input: 

```
tccli waf DescribeTopics --cli-unfold-argument  \
    --Offset 10 \
    --Limit 30
```

Output: 
```
{
    "Response": {
        "Topics": [
            {
                "LogsetId": "46c34030-f7fd-xxxx-91ee-053215c2bf9c",
                "TopicId": "305f8be8-25a9-xxxx-8f05-361dafab39fe",
                "TopicName": "attack-log",
                "PartitionCount": 1,
                "Index": true,
                "AssumerName": "",
                "SubAssumerName": "",
                "CreateTime": "2022-12-30 16:02:52",
                "Status": true,
                "Tags": [],
                "AutoSplit": true,
                "MaxSplitPartitions": 50,
                "StorageType": "hot",
                "Period": 27,
                "Describes": "",
                "HotPeriod": 0,
                "BizType": 0,
                "IsWebTracking": false,
                "Extends": {
                    "AnonymousAccess": null
                }
            }
        ],
        "RequestId": "cdb48d76-9be0-xxxx-8654-56290de7442e",
        "TotalCount": 1
    }
}
```

