**Example 1: 查询云原生API网关实例公网详情**

查询云原生API网关实例公网详情

Input: 

```
tccli tse DescribePublicNetwork --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7 \
    --NetworkId network-z31df1dz
```

Output: 
```
{
    "Response": {
        "RequestId": "534d0349-0663-4dfa-882e-172fe893608e",
        "Result": {
            "GatewayId": "gateway-dde03767",
            "PublicNetwork": {
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
            },
            "GroupId": "group-4se0czf7"
        }
    }
}
```

