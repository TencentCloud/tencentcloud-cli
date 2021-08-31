**Example 1: 获取高危命令列表**

获取高危命令列表

Input: 

```
tccli cwp DescribeBashEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": 1,
                "RuleLevel": 1,
                "Exe": "xx",
                "Uuid": "xx",
                "RuleId": 1,
                "RegexBashCmd": "xx",
                "DetectBy": 1,
                "RuleName": "xx",
                "Pid": "xx",
                "MachineName": "xx",
                "Id": 1,
                "Platform": 1,
                "User": "xx",
                "Hostip": "xx",
                "ModifyTime": "xx",
                "CreateTime": "xx",
                "BashCmd": "xx",
                "RuleCategory": 1,
                "Quuid": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

