**Example 1: 查询参数修改日志**



Input: 

```
tccli cynosdb DescribeClusterParamLogs --cli-unfold-argument  \
    --Limit 0 \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ClusterParamLogs": {
            "Status": "success",
            "CurrentValue": "1024",
            "UpdateTime": "2020-09-22T00:00:00+00:00",
            "UpdateValue": "1025",
            "ParamName": "back_log",
            "CreateTime": "2020-09-22T00:00:00+00:00"
        },
        "TotalCount": 1,
        "RequestId": "651fadd0-7daa-11ec-ae84-e3726d36ffa8"
    }
}
```

