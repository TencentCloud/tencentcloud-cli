**Example 1: 示例**

clickhouse正在运行的查询记录

Input: 

```
tccli tchousex DescribeRunningQuery --cli-unfold-argument  \
    --InstanceId abc \
    --OsUser abc \
    --QueryId abc \
    --SqlKey abc \
    --PageSize 0 \
    --PageNum 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RunningQueryRecords": [
            {
                "NodeIp": "abc",
                "OsUser": "abc",
                "QueryIp": "abc",
                "QueryId": "abc",
                "StartTime": "abc",
                "RunningMs": 0,
                "Sql": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

