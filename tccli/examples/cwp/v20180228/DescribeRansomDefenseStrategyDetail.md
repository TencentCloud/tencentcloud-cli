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
        "RequestId": "c0d89f6e-021b-f1ba-d067-201da364e250",
        "Strategy": {
            "Id": 1,
            "Uin": "100004506473",
            "Name": "tt1",
            "Description": "desc",
            "Status": 1,
            "IsAll": 0,
            "IncludeDir": "/usr",
            "ExcludeDir": "/bin",
            "BackupType": 0,
            "Weekday": "1;2;3;4;5",
            "Hour": "00:00",
            "SaveDay": 0,
            "MachineCount": 1,
            "CreateTime": "2024-04-17 23:19:43",
            "ModifyTime": "2024-10-17 20:10:00",
            "EventCount": 0
        }
    }
}
```

