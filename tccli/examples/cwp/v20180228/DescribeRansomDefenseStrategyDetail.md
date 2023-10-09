**Example 1: 获取策略详情**



Input: 

```
tccli cwp DescribeRansomDefenseStrategyDetail --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Strategy": {
            "Status": 1,
            "ExcludeDir": "xx",
            "Description": "xx",
            "Hour": "xx",
            "EventCount": 1,
            "MachineCount": 1,
            "Uin": "xx",
            "BackupType": 1,
            "IncludeDir": "xx",
            "Weekday": "xx",
            "ModifyTime": "xx",
            "CreateTime": "xx",
            "IsAll": 1,
            "Id": 0,
            "SaveDay": 1,
            "Name": "xx"
        }
    }
}
```

