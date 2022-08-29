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
        "Content": [
            {
                "EnvInfos": [
                    {
                        "VpcInfos": [
                            {
                                "SubnetId": "xx",
                                "VpcId": "xx",
                                "IntranetAddress": "xx"
                            }
                        ],
                        "Status": "xx",
                        "SpecId": "xx",
                        "EnableConfigInternet": true,
                        "EnvDesc": "xx",
                        "ConfigServiceIp": "xx",
                        "StorageCapacity": 0,
                        "EnvName": "xx",
                        "EnvReplica": 0,
                        "ConfigInternetServiceIp": "xx",
                        "AdminServiceIp": "xx",
                        "ClientBandWidth": 1,
                        "AliasEnvName": "xx",
                        "RunningCount": 0
                    }
                ],
                "TradeType": 0,
                "CurDeadline": "xx",
                "AutoRenewFlag": 0,
                "Type": "xx",
                "Edition": "xx",
                "Status": "xx",
                "EnableInternet": true,
                "VpcId": "xx",
                "SpecId": "xx",
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "InstanceId": "xx",
                "EnableConsoleInternet": true,
                "EnableConsoleIntranet": true,
                "EngineRegion": "xx",
                "ConfigInfoVisible": true,
                "IsolateTime": "xx",
                "Name": "xx",
                "ServiceGovernanceInfos": [
                    {
                        "VpcInfos": [
                            {
                                "SubnetId": "xx",
                                "VpcId": "xx",
                                "IntranetAddress": "xx"
                            }
                        ],
                        "BoundK8SInfos": [
                            {
                                "BoundClusterId": "xx",
                                "SyncMode": "xx",
                                "BoundClusterType": "xx"
                            }
                        ],
                        "Features": [
                            "xx"
                        ],
                        "PgwVpcInfos": [
                            {
                                "SubnetId": "xx",
                                "VpcId": "xx",
                                "IntranetAddress": "xx"
                            }
                        ],
                        "AuthOpen": true,
                        "EngineRegion": "xx",
                        "MainPassword": "xx"
                    }
                ],
                "ConsoleDefaultPwd": "xx",
                "StorageCapacity": 0,
                "EKSClusterID": "xx",
                "RegionInfos": [
                    {
                        "Replica": 0,
                        "SpecId": "xx",
                        "EngineRegion": "xx",
                        "EnableClientInternet": true
                    }
                ],
                "StorageType": "xx",
                "SubnetIds": [
                    "xx"
                ],
                "Paymode": "xx",
                "EnableStorage": true,
                "Replica": 0,
                "CreateTime": "xx",
                "VpcInfos": [
                    {
                        "VpcId": "xx",
                        "SubnetId": "xx"
                    }
                ]
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

