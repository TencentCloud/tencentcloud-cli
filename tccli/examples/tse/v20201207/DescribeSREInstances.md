**Example 1: 查询引擎实例列表**

用于查询引擎实例列表

Input: 

```
tccli tse DescribeSREInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Content": [
            {
                "InstanceId": "ins-a123456",
                "Name": "test",
                "Edition": "1.8.6",
                "Status": "creating",
                "SpecId": "spec-id",
                "Replica": 0,
                "Type": "nacos",
                "VpcId": "vpc-id",
                "SubnetIds": [
                    "subnet-id"
                ],
                "EnableStorage": true,
                "StorageType": "SSD",
                "StorageCapacity": 0,
                "Paymode": "POSTPAID",
                "EKSClusterID": "cluster-id",
                "CreateTime": "2021-04-08 10:00:00",
                "EnvInfos": [
                    {
                        "EnvName": "dev",
                        "VpcInfos": [
                            {
                                "VpcId": "vpc-id",
                                "SubnetId": "subnet-id",
                                "IntranetAddress": "10.0.0.1"
                            }
                        ],
                        "Status": "running",
                        "StorageCapacity": 0,
                        "AdminServiceIp": "10.0.0.1",
                        "ConfigServiceIp": "10.0.0.2",
                        "EnableConfigInternet": true,
                        "ConfigInternetServiceIp": "10.0.0.3",
                        "SpecId": "spec-id",
                        "EnvReplica": 0,
                        "RunningCount": 0,
                        "AliasEnvName": "dev-alias",
                        "EnvDesc": "env-desc",
                        "ClientBandWidth": 1,
                        "EnableConfigIntranet": true
                    }
                ],
                "EngineRegion": "ap-guangzhou",
                "EnableInternet": true,
                "VpcInfos": [
                    {
                        "VpcId": "vpc-id",
                        "SubnetId": "subnet-id",
                        "IntranetAddress": "10.0.0.1"
                    }
                ],
                "ServiceGovernanceInfos": [
                    {
                        "EngineRegion": "ap-guangzhou",
                        "BoundK8SInfos": [
                            {
                                "BoundClusterId": "cluster-id",
                                "BoundClusterType": "tke",
                                "SyncMode": "demand",
                                "BindRegion": "ap-guangzhou"
                            }
                        ],
                        "VpcInfos": [
                            {
                                "VpcId": "vpc-id",
                                "SubnetId": "subnet-id",
                                "IntranetAddress": "10.0.0.1"
                            }
                        ],
                        "PgwVpcInfos": [],
                        "LimiterVpcInfos": [],
                        "AuthOpen": true,
                        "Features": [
                            "limit"
                        ],
                        "MainPassword": "password",
                        "CLSTopics": [
                            {
                                "LogSetId": "log-id",
                                "LogSetName": "log-name",
                                "TopicId": "topic-id",
                                "TopicName": "topic-name"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Key": "tag-key",
                        "Value": "tag-value"
                    }
                ],
                "EnableConsoleInternet": true,
                "EnableConsoleIntranet": true,
                "ConfigInfoVisible": true,
                "ConsoleDefaultPwd": "password",
                "TradeType": 0,
                "AutoRenewFlag": 0,
                "CurDeadline": "2024-10-08 10:00:00",
                "IsolateTime": "2024-10-08 12:00:00",
                "RegionInfos": [
                    {
                        "EngineRegion": "ap-guangzhou",
                        "Replica": 0,
                        "SpecId": "spec-id",
                        "EnableClientInternet": true,
                        "MainRegion": true,
                        "ConsoleIntranetVpcInfos": [
                            {
                                "VpcId": "vpc-id",
                                "SubnetId": "subnet-id",
                                "IntranetAddress": "10.0.0.1"
                            }
                        ],
                        "IntranetVpcInfos": [
                            {
                                "VpcId": "vpc-id",
                                "SubnetId": "subnet-id",
                                "IntranetAddress": "10.0.0.1"
                            }
                        ]
                    }
                ],
                "EKSType": "public",
                "FeatureVersion": "STANDARD",
                "EnableClientIntranet": true,
                "StorageOption": [
                    {
                        "Name": "snap",
                        "Type": "SSD",
                        "Capacity": 50
                    }
                ]
            }
        ],
        "RequestId": "req-id"
    }
}
```

