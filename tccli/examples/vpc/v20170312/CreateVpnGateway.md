**Example 1: 创建VPNGW**



Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --VpcId "vpc-xxxx" \
    --VpnGatewayName "test" \
    --InstanceChargeType "POSTPAID_BY_HOUR" \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpnGatewayQuotaSet": [
                {
                    "Bandwidth": 1,
                    "Cname": "xx",
                    "Name": "xx"
                }
            ],
            "MaxConnection": 1,
            "VpcId": "xx",
            "RenewFlag": "xx",
            "Zone": "xx",
            "VpnGatewayName": "xx",
            "InstanceChargeType": "xx",
            "CdcId": "xx",
            "IsAddressBlocked": true,
            "InternetMaxBandwidthOut": 1,
            "State": "xx",
            "Version": "xx",
            "VpnGatewayId": "xx",
            "PublicIpAddress": "xx",
            "CreatedTime": "2020-09-22 00:00:00",
            "NewPurchasePlan": "xx",
            "ExpiredTime": "2020-09-22 00:00:00",
            "Type": "xx",
            "NetworkInstanceId": "xx",
            "RestrictState": "xx"
        },
        "RequestId": "xx"
    }
}
```

