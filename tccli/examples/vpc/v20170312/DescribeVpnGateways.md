**Example 1: 查询VPN网关**



Input: 

```
tccli vpc DescribeVpnGateways --cli-unfold-argument  \
    --Version 2017-03-12 \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-2 ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "VpnGatewaySet": [
            {
                "VpcId": "vpc-ah9e9qu9",
                "VpnGatewayId": "vpngw-5aluhh9t",
                "VpnGatewayName": "joantest",
                "Type": "IPSEC",
                "State": "DELETING",
                "PublicIpAddress": "",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "PREPAID",
                "InternetMaxBandwidthOut": 0,
                "CreatedTime": "2015-08-20 19:39:01",
                "ExpiredTime": "0000-00-00 00:00:00",
                "IsAddressBlocked": false,
                "NewPurchasePlan": "",
                "RestrictState": "NORMAL",
                "Zone": "ap-guangzhou-2",
                "VpnGatewayQuotaSet": [
                    {
                        "Bandwidth": 5,
                        "Cname": "微小型",
                        "Name": "mini"
                    },
                    {
                        "Bandwidth": 20,
                        "Cname": "中型",
                        "Name": "middle"
                    },
                    {
                        "Bandwidth": 100,
                        "Cname": "超大型",
                        "Name": "superLarge"
                    },
                    {
                        "Bandwidth": 10,
                        "Cname": "小型",
                        "Name": "small"
                    },
                    {
                        "Bandwidth": 50,
                        "Cname": "大型",
                        "Name": "large"
                    }
                ]
            },
            {
                "VpcId": "vpc-5rkcp0wb",
                "VpnGatewayId": "vpngw-97yhzme3",
                "VpnGatewayName": "leohli-simulate3",
                "Type": "IPSEC",
                "State": "AVAILABLE",
                "PublicIpAddress": "",
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "InstanceChargeType": "PREPAID",
                "InternetMaxBandwidthOut": 10,
                "CreatedTime": "2017-07-03 14:39:16",
                "ExpiredTime": "2018-05-31 13:03:47",
                "IsAddressBlocked": false,
                "NewPurchasePlan": "PREPAID_TO_POSTPAID",
                "RestrictState": "PROTECTIVELY_ISOLATED",
                "Zone": "ap-guangzhou-3",
                "VpnGatewayQuotaSet": [
                    {
                        "Bandwidth": 5,
                        "Cname": "微小型",
                        "Name": "mini"
                    },
                    {
                        "Bandwidth": 20,
                        "Cname": "中型",
                        "Name": "middle"
                    },
                    {
                        "Bandwidth": 100,
                        "Cname": "超大型",
                        "Name": "superLarge"
                    },
                    {
                        "Bandwidth": 10,
                        "Cname": "小型",
                        "Name": "small"
                    },
                    {
                        "Bandwidth": 50,
                        "Cname": "大型",
                        "Name": "large"
                    }
                ]
            }
        ],
        "RequestId": "feb949ef-8eb8-4eda-ba73-4fc5705bf8f5"
    }
}
```

