**Example 1: 查询代理信息**



Input: 

```
tccli cdb DescribeCdbProxyInfo --cli-unfold-argument  \
    --InstanceId cdb-aykuksx3
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "ProxyInfos": [
            {
                "Status": "xx",
                "ProxyGroupId": "xx",
                "ProxyVersion": "xx",
                "ProxyAddress": [
                    {
                        "MaxDelay": 1,
                        "ProxyAllocation": [
                            {
                                "Region": "xx",
                                "ProxyInstance": [
                                    {
                                        "Status": "xx",
                                        "Zone": "xx",
                                        "Weight": 1,
                                        "InstanceId": "xx",
                                        "Region": "xx",
                                        "InstanceName": "xx",
                                        "InstanceType": "xx"
                                    }
                                ],
                                "Zone": "xx"
                            }
                        ],
                        "UniqVpcId": "xx",
                        "IsKickOut": true,
                        "ReadOnly": true,
                        "ProxyAddressId": "xx",
                        "Vip": "xx",
                        "UniqSubnetId": "xx",
                        "TransSplit": true,
                        "MinCount": 1,
                        "AutoAddRo": true,
                        "VPort": 1,
                        "WeightMode": "xx",
                        "Desc": "xx"
                    }
                ],
                "TaskStatus": "xx",
                "SupportUpgradeProxyVersion": "xx",
                "ProxyNode": [
                    {
                        "Status": "xx",
                        "Zone": "xx",
                        "ProxyId": "xx",
                        "Region": "xx",
                        "Mem": 1,
                        "Connection": 1,
                        "Cpu": 1
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

