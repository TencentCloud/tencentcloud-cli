**Example 1: 查询指定资源组信息**

查询指定资源组信息

Input: 

```
tccli dlc DescribeStandardEngineResourceGroups --cli-unfold-argument  \
    --Filters.0.Name engine-resource-group-id \
    --Filters.0.Values rg-9y1f952gsss
```

Output: 
```
{
    "Response": {
        "RequestId": "21f32ad0-941c-4515-970c-1658f2a19964",
        "Total": 1,
        "UserEngineResourceGroupInfos": [
            {
                "AutoLaunch": 1,
                "AutoPause": 1,
                "AutoPauseTime": 0,
                "CreateTime": 1705892615,
                "Creator": "100013032040",
                "DataEngineId": "DataEngine-37sutfj4",
                "DataEngineName": "spark_common_two",
                "DriverCuSpec": "small",
                "EngineResourceGroupId": "rg-9y1f952g",
                "EngineResourceGroupName": "rg-test",
                "ExecutorCuSpec": "small",
                "MaxExecutorNums": 1,
                "MinExecutorNums": 1,
                "MaxConcurrency": 5,
                "NeedRestart": 0,
                "ResourceGroupState": 0,
                "UpdateTime": 1705892615
            }
        ]
    }
}
```

