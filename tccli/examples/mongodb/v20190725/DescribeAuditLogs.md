**Example 1: 查询审计日志**



Input: 

```
tccli mongodb DescribeAuditLogs --cli-unfold-argument  \
    --InstanceId cmgo-f0vo457l \
    --StartTime 2022-09-28 14:25:38 \
    --EndTime 2026-09-28 15:25:38 \
    --Filter.Atype insert \
    --Filter.Result 0 \
    --Filter.Param insert
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AffectRows": 2,
                "Atype": "insert",
                "ExecTime": 0,
                "Host": "10.0.xx.xx",
                "Param": "{ ns: dbinsert_2.collinsert_1, cmd: { _id: ObjectId('1'), df: [ \"sw\", \"re\" ], likes: 100, title: 3 } }",
                "Result": 0,
                "Roles": "xxx@admin",
                "Timestamp": "2026-01-27 10:54:17",
                "User": "mongouser@xxx"
            }
        ],
        "TotalCount": 2,
        "RequestId": "184c371f-8635-4af9-881b-d0f29856c0f7"
    }
}
```

