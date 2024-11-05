**Example 1: 示例**



Input: 

```
tccli cwp DescribeFileTamperEventRuleInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "FileTamperRuleDetail": {
            "Id": 11855,
            "Uuids": [
                "7168bc08-c1b8-11ea-9053-48fd8e5f474c"
            ],
            "Name": "vim",
            "Rule": [
                {
                    "ProcessPath": "*/vim",
                    "Target": "/home/test/*",
                    "Action": "alert",
                    "FileAction": "read;write"
                }
            ],
            "IsGlobal": 0,
            "Status": 0,
            "Level": 1,
            "CreateTime": "2024-05-29T09:49:10+08:00",
            "ModifyTime": "2024-06-03T20:14:59+08:00",
            "UuidTotalCount": 1,
            "AddWhiteType": "all"
        },
        "RequestId": "f4716f03-cca5-4087-afe8-26f361193661"
    }
}
```

