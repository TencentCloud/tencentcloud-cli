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
            "VpnGatewayId": "vpngw-awdawc",
            "VpcId": "vpc-adxczc",
            "VpnGatewayName": "vpn-name",
            "Type": "IPSEC",
            "State": "Pending",
            "PublicIpAddress": "13.15.41.4",
            "RenewFlag": "",
            "InstanceChargeType": "POSTPAID_BY_HOUR",
            "InternetMaxBandwidthOut": 10,
            "CreatedTime": "2020-09-22 00:00:00",
            "ExpiredTime": "2020-09-22 00:00:00",
            "IsAddressBlocked": false,
            "NewPurchasePlan": "",
            "RestrictState": "NORMAL",
            "Zone": "",
            "VpnGatewayQuotaSet": [
                {
                    "Bandwidth": 5,
                    "Cname": "微小型",
                    "Name": "cdmini"
                }
            ],
            "Version": "ver3.1",
            "NetworkInstanceId": "",
            "CdcId": "",
            "MaxConnection": 10
        },
        "RequestId": "b2187525-ab9d-42cb-82ee-998ead365bbe"
    }
}
```

