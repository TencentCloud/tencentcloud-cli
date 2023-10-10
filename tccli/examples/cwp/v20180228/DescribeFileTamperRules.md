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
                "Name": "xx",
                "HostCount": 1,
                "ModifyTime": "xx",
                "CreateTime": "xx",
                "RuleCategory": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

