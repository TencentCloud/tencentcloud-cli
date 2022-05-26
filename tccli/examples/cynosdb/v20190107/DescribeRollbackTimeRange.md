**Example 1: 查询有效回归时间范围**



Input: 

```
tccli cynosdb DescribeRollbackTimeRange --cli-unfold-argument  \
    --ClusterId cynosdbmysql-oib3wx0i
```

Output: 
```
{
    "Response": {
        "TimeRangeStart": "2019-01-13 02:12:05",
        "TimeRangeEnd": "2019-01-20 02:10:12",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

