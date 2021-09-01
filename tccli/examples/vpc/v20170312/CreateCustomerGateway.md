**Example 1: 创建对端网关**



Input: 

```
tccli vpc CreateCustomerGateway --cli-unfold-argument  \
    --Version 2017-03-12 \
    --CustomerGatewayName test-cgw \
    --IpAddress 58.211.1.12 \
    --Tags.0.Key city \
    --Tags.0.Value shanghai
```

Output: 
```
{
    "Response": {
        "CustomerGateway": {
            "CustomerGatewayId": "cgw-mgp33pll",
            "IpAddress": "58.211.1.12",
            "CustomerGatewayName": "test-cgw"
        },
        "RequestId": "5bd98433-263a-47b6-9a1c-84aa613a8ff6"
    }
}
```

