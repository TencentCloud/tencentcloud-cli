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
                "Id": 0,
                "Uin": "abc",
                "Name": "abc",
                "Description": "abc",
                "Status": 1,
                "IsAll": 1,
                "IncludeDir": "abc",
                "ExcludeDir": "abc",
                "BackupType": 1,
                "Weekday": "abc",
                "Hour": "abc",
                "SaveDay": 1,
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "MachineCount": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

