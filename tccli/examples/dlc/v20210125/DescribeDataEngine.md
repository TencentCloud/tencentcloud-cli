**Example 1: test**



Input: 

```
tccli dlc DescribeDataEngine --cli-unfold-argument  \
    --DataEngineName public-engine
```

Output: 
```
{
    "Response": {
        "DataEngine": {
            "DataEngineName": "abc",
            "EngineType": "abc",
            "ClusterType": "abc",
            "QuotaId": "abc",
            "State": 0,
            "CreateTime": 0,
            "UpdateTime": 0,
            "Size": 0,
            "Mode": 0,
            "MinClusters": 0,
            "MaxClusters": 0,
            "AutoResume": true,
            "SpendAfter": 0,
            "CidrBlock": "abc",
            "DefaultDataEngine": true,
            "Message": "abc",
            "DataEngineId": "abc",
            "SubAccountUin": "abc",
            "ExpireTime": "abc",
            "IsolatedTime": "abc",
            "ReversalTime": "abc",
            "UserAlias": "abc",
            "TagList": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "Permissions": [
                "abc"
            ],
            "AutoSuspend": true,
            "CrontabResumeSuspend": 0,
            "CrontabResumeSuspendStrategy": {
                "ResumeTime": "abc",
                "SuspendTime": "abc",
                "SuspendStrategy": 0
            },
            "EngineExecType": "abc",
            "RenewFlag": 0,
            "AutoSuspendTime": 0,
            "NetworkConnectionSet": [
                {
                    "Id": 0,
                    "AssociateId": "abc",
                    "HouseId": "abc",
                    "DatasourceConnectionId": "abc",
                    "State": 0,
                    "CreateTime": 0,
                    "UpdateTime": 0,
                    "Appid": 0,
                    "HouseName": "abc",
                    "DatasourceConnectionName": "abc",
                    "NetworkConnectionType": 0,
                    "Uin": "abc",
                    "SubAccountUin": "abc",
                    "NetworkConnectionDesc": "abc",
                    "DatasourceConnectionVpcId": "abc",
                    "DatasourceConnectionSubnetId": "abc",
                    "DatasourceConnectionCidrBlock": "abc",
                    "DatasourceConnectionSubnetCidrBlock": "abc"
                }
            ],
            "UiURL": "abc",
            "ResourceType": "abc",
            "ImageVersionId": "abc",
            "ChildImageVersionId": "abc",
            "ImageVersionName": "abc",
            "StartStandbyCluster": true,
            "ElasticSwitch": true,
            "ElasticLimit": 0,
            "DefaultHouse": true,
            "MaxConcurrency": 0,
            "TolerableQueueTime": 0,
            "UserAppId": 0,
            "UserUin": "abc",
            "SessionResourceTemplate": {
                "DriverSize": "abc",
                "ExecutorSize": "abc",
                "ExecutorNums": 1,
                "ExecutorMaxNumbers": 1
            },
            "AutoAuthorization": true,
            "EngineGeneration": "abc",
            "EngineTypeDetail": "abc",
            "EngineNetworkId": "abc",
            "EngineResourceGroupCount": 0,
            "EngineResourceUsedCU": 0,
            "AccessInfos": [
                {
                    "AccessType": "abc",
                    "AccessConnectionInfos": [
                        "abc"
                    ]
                }
            ],
            "EngineNetworkName": "abc"
        },
        "RequestId": "abc"
    }
}
```

