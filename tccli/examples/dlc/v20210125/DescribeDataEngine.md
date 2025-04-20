**Example 1: 获取数据引擎详细信息**

获取数据引擎详细信息

Input: 

```
tccli dlc DescribeDataEngine --cli-unfold-argument  \
    --DataEngineName dlc-spark
```

Output: 
```
{
    "Response": {
        "DataEngine": {
            "AccessInfos": null,
            "AutoAuthorization": true,
            "AutoResume": false,
            "AutoSuspend": false,
            "AutoSuspendTime": 10,
            "ChildImageVersionId": "681fab43-a79c-42ec-9c7b-42917af33611",
            "CidrBlock": "10.0.0.0/16",
            "ClusterType": "spark_cu",
            "CreateTime": 1735872007,
            "CrontabResumeSuspend": 0,
            "CrontabResumeSuspendStrategy": {
                "ResumeTime": "",
                "SuspendStrategy": 0,
                "SuspendTime": ""
            },
            "DataEngineId": "DataEngine-houseid",
            "DataEngineName": "dlc-spark",
            "DefaultDataEngine": false,
            "DefaultHouse": false,
            "ElasticLimit": 0,
            "ElasticSwitch": false,
            "EngineExecType": "BATCH",
            "EngineGeneration": "Native",
            "EngineNetworkId": "DataEngine-Networkid",
            "EngineNetworkName": "",
            "EngineResourceGroupCount": 0,
            "EngineResourceUsedCU": 0,
            "EngineType": "spark",
            "EngineTypeDetail": "StandardSpark",
            "ExpireTime": "0",
            "GatewayId": "DataEngine-gatewayid",
            "GatewayState": 2,
            "ImageVersionId": "c3a40d9a-f5fe-40ac-9c17-16fed3fd2644",
            "ImageVersionName": "Standard-S 1.1",
            "IsAIEngine": 1,
            "IsAIGateway": true,
            "IsPoolMode": null,
            "IsSupportAI": false,
            "IsolatedTime": "0",
            "MaxClusters": 1,
            "MaxConcurrency": 5,
            "Message": "",
            "MinClusters": 1,
            "Mode": 1,
            "NetworkConnectionSet": [],
            "Permissions": [
                "USE",
                "MODIFY",
                "OPERATE",
                "MONITOR",
                "DELETE"
            ],
            "QuotaId": "",
            "RenewFlag": 0,
            "ResourceType": "Standard_CU",
            "ReversalTime": "0",
            "SessionResourceTemplate": {
                "DriverSize": "large",
                "ExecutorMaxNumbers": 3,
                "ExecutorNums": 3,
                "ExecutorSize": "large"
            },
            "Size": 16,
            "SpendAfter": 0,
            "StartStandbyCluster": false,
            "State": 2,
            "SubAccountUin": "1000****2040",
            "TagList": [],
            "TolerableQueueTime": 0,
            "UiURL": "-1",
            "UpdateTime": 1735872007,
            "UserAlias": "1000****2040",
            "UserAppId": "1301234123",
            "UserUin": "1000****7117"
        },
        "RequestId": "b040e00f-9f7f-46c1-a7aa-5e3382225d62"
    }
}
```

