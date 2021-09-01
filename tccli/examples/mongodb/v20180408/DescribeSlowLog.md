**Example 1: 查询云数据库MongoDB实例慢日志**

客户需要通过API查询云数据库MongoDB实例慢日志

Input: 

```
tccli mongodb DescribeSlowLog --cli-unfold-argument  \
    --InstanceId cmgo-eqmoa5sf \
    --StartTime '2019-06-04 20:21:00' \
    --EndTime '2019-06-04 20:22:00' \
    --SlowMS 200 \
    --Offset 20 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "302530d2-ee57-495e-89d0-51e03b11815e",
        "SlowLogList": [
            "Tue Jun  4 17:52:39.247 I COMMAND  [conn2898] xxxx"
        ]
    }
}
```

