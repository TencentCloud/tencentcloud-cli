**Example 1: 测试获取云原生API网关配置信息**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayConfig --cli-unfold-argument  \
    --GatewayId gateway-dde03767
```

Output: 
```
{
    "Response": {
        "RequestId": "534d0349-0663-4dfa-882e-172fe893608e",
        "Result": {
            "GatewayId": "gateway-dde03767",
            "ConfigList": [
                {
                    "ConsoleType": "Konga",
                    "NetType": "Open",
                    "Status": "Open",
                    "AccessControl": {
                        "Mode": "Whitelist",
                        "CidrWhiteList": [
                            "0.0.0.0"
                        ],
                        "CidrBlackList": []
                    },
                    "VpcId": "",
                    "SubnetId": "",
                    "HttpUrl": "",
                    "HttpsUrl": "https://gateway-dde03767-konga.gz.apigw.tencentcs.com:1337/",
                    "AdminUser": "admin",
                    "AdminPassword": "husdqwe1zd3sjwSIx4@",
                    "Vip": "",
                    "InternetMaxBandwidthOut": 0,
                    "Description": "",
                    "SlaType": "",
                    "SlaName": "",
                    "MultiZoneFlag": false,
                    "MasterZoneId": "",
                    "SlaveZoneId": "",
                    "MasterZoneName": "",
                    "SlaveZoneName": "",
                    "NetworkId": ""
                }
            ],
            "GroupVpcId": "vpc-k0dl0rk1",
            "GroupSubnetId": "subnet-ec94pnyu",
            "GroupId": "group-d2bdcff3"
        }
    }
}
```

