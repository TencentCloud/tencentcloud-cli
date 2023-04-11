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

**Example 2: 高危命令事件列表**



Input: 

```
tccli cwp DescribeBashEvents --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Uuid": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
                "Id": 3148114,
                "Quuid": "02db9a21-78fe-4a4c-b96f-a11bf819a962",
                "Hostip": "192.168.111.28",
                "User": "root",
                "Platform": 4,
                "BashCmd": "./r3hook_tool moc -var www.test123.com",
                "RuleId": 0,
                "RuleName": "sysrule_custom_procmon_1",
                "RuleLevel": 1,
                "Status": 0,
                "CreateTime": "2022-09-01 17:28:39",
                "MachineName": "v_llzlu恶意请求",
                "DetectBy": 0,
                "Pid": "0",
                "Exe": "",
                "ModifyTime": "0001-01-01 00:00:00",
                "RegexBashCmd": "\\./r3hook_tool moc -var www\\.test123\\.com",
                "RuleCategory": 0
            }
        ],
        "RequestId": "c787b780-0a35-4fa5-aca3-db339b9a20e8",
        "TotalCount": 51315
    }
}
```

