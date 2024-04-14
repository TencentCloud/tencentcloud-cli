**Example 1: 查询按照时间点可回档的时间范围。**

本接口(DescribeRestoreTimeRange)用于查询按照时间点可回档的时间范围。

Input: 

```
tccli sqlserver DescribeRestoreTimeRange --cli-unfold-argument  \
    --InstanceId mssql-aj89iq78 \
    --TargetInstanceId mssql-jkoa09sf
```

Output: 
```
{
    "Response": {
        "MinTime": "2024-01-01 00:00:00",
        "MaxTime": "2024-01-07 00:00:00",
        "RequestId": "cd7a35be-2fbf-f3a6-210a-ea9afe158817"
    }
}
```

