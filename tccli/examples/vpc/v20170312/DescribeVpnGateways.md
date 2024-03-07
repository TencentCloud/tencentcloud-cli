**Example 1: 查询VPN网关**

本接口（DescribeVpnGateways）用于查询VPN网关列表。

Input: 

```
tccli vpc DescribeVpnGateways --cli-unfold-argument  \
    --VpnGatewayIds vpngw-xxxxx \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpnGatewaySet": [
            {
                "VpnGatewayId": "vpngw-xxxx",
                "VpcId": "vpc-xxxx",
                "VpnGatewayName": "vpn_name",
                "Type": "CCN",
                "State": "AVAILABLE",
                "PublicIpAddress": "142.133.53.16",
                "RenewFlag": "NOTIFY_AND_AUTO_RENEW",
                "InstanceChargeType": "POSTPAID_BY_HOUR",
                "InternetMaxBandwidthOut": 10,
                "CreatedTime": "2020-09-22 00:00:00",
                "ExpiredTime": "2020-09-22 00:00:00",
                "IsAddressBlocked": false,
                "NewPurchasePlan": "",
                "RestrictState": "NORMAL",
                "Zone": "ap-beijing-1",
                "VpnGatewayQuotaSet": [
                    {
                        "Bandwidth": 5,
                        "Cname": "微小型",
                        "Name": "cdmini"
                    },
                    {
                        "Bandwidth": 20,
                        "Cname": "中型",
                        "Name": "cdmiddle"
                    },
                    {
                        "Bandwidth": 50,
                        "Cname": "大型",
                        "Name": "cdlarge"
                    },
                    {
                        "Bandwidth": 10,
                        "Cname": "小型",
                        "Name": "cdsmall"
                    },
                    {
                        "Bandwidth": 100,
                        "Cname": "超大型",
                        "Name": "cdsuperLarge"
                    },
                    {
                        "Bandwidth": 1000,
                        "Cname": "超大型4",
                        "Name": "cdsuperLarge4"
                    },
                    {
                        "Bandwidth": 200,
                        "Cname": "超大型2",
                        "Name": "cdsuperLarge2"
                    },
                    {
                        "Bandwidth": 500,
                        "Cname": "超大型3",
                        "Name": "cdsuperLarge3"
                    },
                    {
                        "Bandwidth": 3000,
                        "Cname": "超大型5",
                        "Name": "cdsuperLarge5"
                    }
                ],
                "Version": "abc",
                "NetworkInstanceId": "abc",
                "CdcId": "abc",
                "MaxConnection": 5
            }
        ],
        "RequestId": "dc43b486-80aa-4cf0-9f8a-4b95e9092685"
    }
}
```

