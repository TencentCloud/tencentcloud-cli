**Example 1: 查询实例参数修改历史**



Input: 

```
tccli sqlserver DescribeInstanceParamRecords --cli-unfold-argument  \
    --InstanceId mssql-bm5e51kb \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "InstanceId": "mssql-bm5e51kb",
                "ModifyTime": "2021-04-09 19:04:12",
                "NewValue": "60",
                "OldValue": "80",
                "ParamName": "fill factor(%)",
                "Status": 3
            },
            {
                "InstanceId": "mssql-bm5e51kb",
                "ModifyTime": "2021-04-09 20:26:57",
                "NewValue": "60",
                "OldValue": "80",
                "ParamName": "fill factor(%)",
                "Status": 3
            }
        ],
        "RequestId": "10684c55-95b7-40de-b070-23f02c6746d2",
        "TotalCount": 2
    }
}
```

