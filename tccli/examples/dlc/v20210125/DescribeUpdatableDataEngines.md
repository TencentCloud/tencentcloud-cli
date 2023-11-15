**Example 1: 查询需要更新结果桶集群配置的sparksql引擎**

查询需要更新结果桶集群配置的sparksql引擎

Input: 

```
tccli dlc DescribeUpdatableDataEngines --cli-unfold-argument  \
    --DataEngineConfigCommand UpdateSparkSQLResultPath
```

Output: 
```
{
    "Response": {
        "DataEngineBasicInfos": [
            {
                "DataEngineName": "abc",
                "State": 0,
                "CreateTime": 0,
                "UpdateTime": 0,
                "Message": "abc",
                "DataEngineId": "abc",
                "DataEngineType": "abc",
                "AppId": 0,
                "UserUin": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

