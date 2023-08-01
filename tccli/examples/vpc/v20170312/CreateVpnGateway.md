**Example 1: 创建VPNGW**

创建VPNGW

Input: 

```
tccli vpc CreateVpnGateway --cli-unfold-argument  \
    --VpnGatewayName "test" \
    --VpcId "vpc-xxxx" \
    --InstanceChargeType "POSTPAID_BY_HOUR" \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "VpnGateway": {
            "VpnGatewayQuotaSet": [],
            "MaxConnection": 5,
            "VpcId": "vpc-test",
            "RenewFlag": "",
            "Zone": "ap-bangkok-1",
            "VpnGatewayName": "test",
            "InstanceChargeType": "POSTPAID_BY_HOUR",
            "CdcId": "",
            "IsAddressBlocked": true,
            "InternetMaxBandwidthOut": 10,
            "State": "Pending",
            "Version": "",
            "VpnGatewayId": "vpngw-xxxxx",
            "PublicIpAddress": "12.3.1.3",
            "CreatedTime": "2020-09-22 00:00:00",
            "NewPurchasePlan": "",
            "ExpiredTime": "2020-09-22 00:00:00",
            "Type": "IPSEC",
            "NetworkInstanceId": "",
            "RestrictState": "NORMAL"
        },
        "RequestId": "fa15cd12-e329-1261-c585-3c3ae5c55211"
    }
}
```

