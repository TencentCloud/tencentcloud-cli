**Example 1: 查询DataEngines信息列表**

查询DataEngines信息列表

Input: 

```
tccli dlc DescribeDataEngines --cli-unfold-argument  \
    --Sorting desc \
    --Limit 10 \
    --SortBy create-time \
    --Filters.0.Values engine-type \
    --Filters.0.Name presto \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DataEngines": [
            {
                "MaxClusters": 10,
                "DefaultDataEngine": true,
                "UpdateTime": 1635320563,
                "SpendAfter": 10,
                "DataEngineId": "****",
                "CidrBlock": "10.255.252.0/22",
                "SubAccountUin": "****",
                "AutoResume": true,
                "ClusterType": "presto_private",
                "QuotaId": "****",
                "State": 0,
                "DataEngineName": "shared_presto",
                "Mode": 0,
                "Message": "测试资源",
                "CreateTime": 1635320563,
                "EngineType": "presto",
                "MinClusters": 0,
                "Size": 64
            }
        ],
        "RequestId": "2f67771a-a384-4b4e-86a5-146d8829ae2d"
    }
}
```

