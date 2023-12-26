**Example 1: 核心文件监控事件列表**



Input: 

```
tccli cwp DescribeFileTamperRules --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Status": 1,
                "Name": "核心文件名称1",
                "HostCount": 1,
                "ModifyTime": "2023-01-01 00:00:00",
                "CreateTime": "2023-01-01 00:00:00",
                "RuleCategory": 1,
                "Id": 1,
                "IsGlobal": 1,
                "Level": 1,
                "WriteRuleCount": 1,
                "ReadRuleCount": 1,
                "ReadWriteRuleCount": 1,
                "FileAction": "",
                "AddWhiteType": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

