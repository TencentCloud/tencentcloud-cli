**Example 1: 查询参数修改记录**



Input: 

```
tccli cynosdb DescribeClusterParamLogs --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg712eh \
    --InstanceIds cynosdbmysql-ins-m6f0hkdb \
    --OrderBy CreateTime \
    --OrderByType DESC \
    --Limit 12 \
    --Offset 12
```

Output: 
```
{
    "Response": {
        "ClusterParamLogs": [
            {
                "Status": "success",
                "CurrentValue": "1024",
                "UpdateTime": "2020-09-22T00:00:00+00:00",
                "UpdateValue": "1025",
                "ParamName": "back_log",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ClusterId": "cynosdbmysql-mwg712eh",
                "InstanceId": "cynosdbmysql-ins-m6f0hkdb"
            }
        ],
        "TotalCount": 1,
        "RequestId": "651fadd0-7daa-11ec-ae84-e3726d36ffa8"
    }
}
```

