**Example 1: 查询对端网关**

查询对端网关

Input: 

```
tccli vpc DescribeCustomerGateways --cli-unfold-argument  \
    --CustomerGatewayIds cgw-mgp33pll \
    --Filters.0.Name customer-gateway-name \
    --Filters.0.Values test-cgw \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "CustomerGatewaySet": [
            {
                "CustomerGatewayId": "cgw-mgp33pll",
                "IpAddress": "58.211.1.12",
                "CustomerGatewayName": "test-cgw",
                "CreatedTime": "2018-03-25 17:52:39"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e5500b60-4964-43c7-8a6c-4bff98f59aeb"
    }
}
```

