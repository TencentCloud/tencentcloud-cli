**Example 1: test**



Input: 

```
tccli dlc DescribeDataEngine --cli-unfold-argument  \
    --DataEngineName xx
```

Output: 
```
{
    "Response": {
        "DataEngine": {
            "MaxClusters": 0,
            "DefaultDataEngine": true,
            "UpdateTime": 0,
            "SpendAfter": 0,
            "DataEngineId": "xx",
            "CidrBlock": "xx",
            "SubAccountUin": "xx",
            "AutoResume": true,
            "ClusterType": "xx",
            "QuotaId": "xx",
            "State": 0,
            "DataEngineName": "xx",
            "Mode": 0,
            "Message": "xx",
            "CreateTime": 0,
            "EngineType": "xx",
            "MinClusters": 0,
            "Size": 0
        },
        "RequestId": "xx"
    }
}
```

