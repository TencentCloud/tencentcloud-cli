**Example 1: 查询需要更新结果桶集群配置的sparksql引擎**

查询需要更新结果桶集群配置的sparksql引擎

Input: 

```
tccli dlc DescribeUpdatableDataEngines --cli-unfold-argument  \
    --DataEngineConfigCommand UpdateTaskResultPath \
    --UseLakeFs True \
    --CustomResultPath cosn://test-bucket/dir
```

Output: 
```
{
    "Response": {
        "DataEngineBasicInfos": [
            {
                "DataEngineId": "DataEngine-houseid1",
                "DataEngineName": "SparkSQL",
                "AppId": 130001173,
                "UserUin": "1000117",
                "State": 2,
                "CreateTime": 1729758961,
                "UpdateTime": 1729758961,
                "Message": "",
                "DataEngineType": "SparkSQL"
            }
        ],
        "RequestId": "5441bd1b-af71-4bd1-97f0-33568cf387b7",
        "TotalCount": 1
    }
}
```

