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
                        "ConfigServiceIp": "xx",
                        "StorageCapacity": 0,
                        "EnvName": "xx",
                        "EnvReplica": 0,
                        "ConfigInternetServiceIp": "xx",
                        "AdminServiceIp": "xx",
                        "RunningCount": 0
                    }
                ],
                "Type": "xx",
                "Edition": "xx",
                "Status": "xx",
                "EnableConsoleIntranet": true,
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
                "EngineRegion": "xx",
                "ConfigInfoVisible": true,
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
                                "BoundClusterType": "xx"
                            }
                        ],
                        "AuthOpen": true,
                        "EngineRegion": "xx",
                        "Features": [
                            "xx"
                        ]
                    }
                ],
                "StorageCapacity": 0,
                "EKSClusterID": "xx",
                "VpcInfos": [
                    {
                        "SubnetId": "xx",
                        "VpcId": "xx",
                        "IntranetAddress": "xx"
                    }
                ],
                "StorageType": "xx",
                "SubnetIds": [
                    "a"
                ],
                "Paymode": "xx",
                "EnableStorage": true,
                "Replica": 3,
                "EnableInternet": true,
                "CreateTime": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

