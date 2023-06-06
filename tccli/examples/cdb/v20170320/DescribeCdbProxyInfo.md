**Example 1: 查询代理信息**

查询代理信息

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
                "ConnectionPoolLimit": 5,
                "ProxyAddress": [
                    {
                        "AutoAddRo": true,
                        "ConnectionPool": false,
                        "Desc": "",
                        "FailOver": true,
                        "IsKickOut": false,
                        "MaxDelay": 0,
                        "MinCount": 0,
                        "ProxyAddressId": "proxyaddr-test",
                        "ProxyAllocation": [
                            {
                                "ProxyInstance": [
                                    {
                                        "InstanceId": "cdb-test",
                                        "InstanceName": "测试",
                                        "InstanceType": "1",
                                        "Region": "ap-nanjing",
                                        "Status": 1,
                                        "Weight": 0,
                                        "Zone": "ap-nanjing-1"
                                    }
                                ],
                                "Region": "ap-nanjing",
                                "Zone": "ap-nanjing-1"
                            }
                        ],
                        "ReadOnly": false,
                        "TransSplit": false,
                        "UniqSubnetId": "subnet-test",
                        "UniqVpcId": "vpc-test",
                        "VPort": 3306,
                        "Vip": "10.0.0.0",
                        "WeightMode": "custom"
                    }
                ],
                "ProxyGroupId": "proxy-mfxftest",
                "ProxyNode": [
                    {
                        "Cpu": 2,
                        "Mem": 4000,
                        "ProxyId": "proxynode-test",
                        "Region": "ap-nanjing",
                        "Status": "online",
                        "Zone": "ap-nanjing-1",
                        "Connection": 1
                    }
                ],
                "ProxyVersion": "1.3.7",
                "Status": "online",
                "SupportCreateProxyAddress": false,
                "SupportUpgradeProxyMysqlVersion": "20211030",
                "SupportUpgradeProxyVersion": "1.3.7",
                "TaskStatus": "ProxyModifyAddress"
            }
        ],
        "RequestId": "69d4c061-9730-4e2f-btttbb2-a74624bc9a6c"
    }
}
```

