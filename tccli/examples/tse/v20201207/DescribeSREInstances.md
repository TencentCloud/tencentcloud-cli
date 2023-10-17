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
                "InstanceId": "abc",
                "Name": "abc",
                "Edition": "abc",
                "Status": "abc",
                "SpecId": "abc",
                "Replica": 0,
                "Type": "abc",
                "VpcId": "abc",
                "SubnetIds": [
                    "abc"
                ],
                "EnableStorage": true,
                "StorageType": "abc",
                "StorageCapacity": 0,
                "Paymode": "abc",
                "EKSClusterID": "abc",
                "CreateTime": "abc",
                "EnvInfos": [
                    {
                        "EnvName": "abc",
                        "VpcInfos": [
                            {
                                "VpcId": "abc",
                                "SubnetId": "abc",
                                "IntranetAddress": "abc"
                            }
                        ],
                        "Status": "abc",
                        "StorageCapacity": 0,
                        "AdminServiceIp": "abc",
                        "ConfigServiceIp": "abc",
                        "EnableConfigInternet": true,
                        "ConfigInternetServiceIp": "abc",
                        "SpecId": "abc",
                        "EnvReplica": 0,
                        "RunningCount": 0,
                        "AliasEnvName": "abc",
                        "EnvDesc": "abc",
                        "ClientBandWidth": 1,
                        "EnableConfigIntranet": true
                    }
                ],
                "EngineRegion": "abc",
                "EnableInternet": true,
                "VpcInfos": [
                    {
                        "VpcId": "abc",
                        "SubnetId": "abc",
                        "IntranetAddress": "abc"
                    }
                ],
                "ServiceGovernanceInfos": [
                    {
                        "EngineRegion": "abc",
                        "BoundK8SInfos": [
                            {
                                "BoundClusterId": "abc",
                                "BoundClusterType": "abc",
                                "SyncMode": "abc",
                                "BindRegion": "abc"
                            }
                        ],
                        "VpcInfos": [
                            {
                                "VpcId": "abc",
                                "SubnetId": "abc",
                                "IntranetAddress": "abc"
                            }
                        ],
                        "PgwVpcInfos": [],
                        "LimiterVpcInfos": [],
                        "AuthOpen": true,
                        "Features": [
                            "abc"
                        ],
                        "MainPassword": "abc",
                        "CLSTopics": [
                            {
                                "LogSetId": "abc",
                                "LogSetName": "abc",
                                "TopicId": "abc",
                                "TopicName": "abc"
                            }
                        ]
                    }
                ],
                "Tags": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "EnableConsoleInternet": true,
                "EnableConsoleIntranet": true,
                "ConfigInfoVisible": true,
                "ConsoleDefaultPwd": "abc",
                "TradeType": 0,
                "AutoRenewFlag": 0,
                "CurDeadline": "abc",
                "IsolateTime": "abc",
                "RegionInfos": [
                    {
                        "EngineRegion": "abc",
                        "Replica": 0,
                        "SpecId": "abc",
                        "EnableClientInternet": true,
                        "MainRegion": true,
                        "ConsoleIntranetVpcInfos": [
                            {
                                "VpcId": "abc",
                                "SubnetId": "abc",
                                "IntranetAddress": "abc"
                            }
                        ],
                        "IntranetVpcInfos": [
                            {
                                "VpcId": "abc",
                                "SubnetId": "abc",
                                "IntranetAddress": "abc"
                            }
                        ]
                    }
                ],
                "EKSType": "abc",
                "FeatureVersion": "abc",
                "EnableClientIntranet": true,
                "StorageOption": [
                    {
                        "Name": "abc",
                        "Type": "abc",
                        "Capacity": 1
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

