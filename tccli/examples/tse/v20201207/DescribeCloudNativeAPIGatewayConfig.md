**Example 1: 测试获取云原生API网关配置信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConfig --cli-unfold-argument  \
    --GatewayId <GatewayId>
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "ConfigList": [
                {
                    "ConsoleType": "abc",
                    "HttpUrl": "abc",
                    "HttpsUrl": "abc",
                    "NetType": "abc",
                    "AdminUser": "abc",
                    "AdminPassword": "abc",
                    "Status": "abc",
                    "AccessControl": {
                        "Mode": "abc",
                        "CidrWhiteList": [
                            "abc"
                        ],
                        "CidrBlackList": [
                            "abc"
                        ]
                    },
                    "SubnetId": "abc",
                    "VpcId": "abc",
                    "Description": "abc",
                    "SlaType": "abc",
                    "Vip": "abc",
                    "InternetMaxBandwidthOut": 1,
                    "MultiZoneFlag": true,
                    "MasterZoneId": "abc",
                    "SlaveZoneId": "abc",
                    "MasterZoneName": "abc",
                    "SlaveZoneName": "abc",
                    "NetworkId": "abc"
                }
            ],
            "GroupSubnetId": "abc",
            "GroupVpcId": "abc"
        },
        "RequestId": "abc"
    }
}
```

