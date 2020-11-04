**Example 1: 查询对端网关**



Input: 

```
tccli bmvpc DescribeCustomerGateways --cli-unfold-argument  \
    --Version 2018-06-25
```

Output: 
```
{
    "Response": {
        "CustomerGatewaySet": [
            {
                "CustomerGatewayId": "bmcgw-mgp33pll",
                "IpAddress": "58.211.1.12",
                "CustomerGatewayName": "test-cgw",
                "VpnConnNum": 0,
                "CreateTime": "2018-03-25 17:52:39"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e5500b60-4964-43c7-8a6c-4bff98f59aeb"
    }
}
```

