**Example 1: 查询云原生API网关实例公网详情**

查询云原生API网关实例公网详情

Input: 

```
tccli tse DescribePublicNetwork --cli-unfold-argument  \
    --GatewayId gateway-xxxxxxxx \
    --GroupId greoup-xxxxxxxx \
    --NetworkId network-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "GroupId": "abc",
            "PublicNetwork": {
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
                "SlaName": "abc",
                "Vip": "abc",
                "InternetMaxBandwidthOut": 1,
                "MultiZoneFlag": true,
                "MasterZoneId": "abc",
                "SlaveZoneId": "abc",
                "MasterZoneName": "abc",
                "SlaveZoneName": "abc",
                "NetworkId": "abc"
            }
        },
        "RequestId": "abc"
    }
}
```

