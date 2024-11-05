**Example 1: 示例**



Input: 

```
tccli cwp DescribeFileTamperRuleInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "FileTamperRuleDetail": {
            "Id": 10001,
            "Uuids": [
                "1ce68339-8828-457f-b358-d5b1b34e4fe9"
            ],
            "Name": "机器名称",
            "Rule": [
                {
                    "ProcessPath": "*/vi",
                    "Target": "/root/*",
                    "Action": "alert",
                    "FileAction": "write"
                }
            ],
            "IsGlobal": 0,
            "Status": 1,
            "CreateTime": "2024-08-23T14:37:10+08:00",
            "ModifyTime": "2024-10-10T20:38:26+08:00",
            "Level": 1,
            "UuidTotalCount": 1,
            "AddWhiteType": "all"
        },
        "RequestId": "2725aee8-adc4-4501-90cd-ccd77bfd35d5"
    }
}
```

