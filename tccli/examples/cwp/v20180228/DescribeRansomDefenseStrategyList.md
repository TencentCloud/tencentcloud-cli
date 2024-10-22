**Example 1: 查询防勒索策略列表**

查询防勒索策略列表

Input: 

```
tccli cwp DescribeRansomDefenseStrategyList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 5570,
                "Uin": "3232323",
                "Name": "tt1",
                "Description": "",
                "Status": 1,
                "IsAll": 0,
                "IncludeDir": "/",
                "ExcludeDir": "",
                "BackupType": 0,
                "Weekday": "1;2;3;4;5",
                "Hour": "00:00",
                "SaveDay": 0,
                "MachineCount": 1,
                "CreateTime": "2024-04-17 23:19:43",
                "ModifyTime": "2024-10-17 20:10:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

