**Example 1: 查询VPN网关**



Input: 

```
tccli bmvpc DescribeVpnGateways --cli-unfold-argument  \
    --Version 2018-06-25 \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpnGatewaySet": [
            {
                "VpcId": "vpc-ah9e9qu9",
                "VpnGatewayId": "bmvpngw-5aluhh9t",
                "VpnGatewayName": "joantest",
                "State": 0,
                "PublicIpAddress": "",
                "InternetMaxBandwidthOut": 100,
                "CreateTime": "2015-08-20 19:39:01",
                "VpcName": "test",
                "VpcCidrBlock": "172.16.0.0/16",
                "VpnConnNum": 2,
                "Zone": "ap-guangzhou"
            }
        ],
        "RequestId": "feb949ef-8eb8-4eda-ba73-4fc5705bf8f5"
    }
}
```

