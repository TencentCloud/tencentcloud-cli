**Example 1: Querying customer gateways**



Input: 

```
tccli vpc DescribeCustomerGateways --cli-unfold-argument  \
    --Version 2017-03-12
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

