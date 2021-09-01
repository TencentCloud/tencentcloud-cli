**Example 1: 创建对端网关**



Input: 

```
tccli bmvpc CreateCustomerGateway --cli-unfold-argument  \
    --Version 2018-06-25 \
    --CustomerGatewayName test-cgw \
    --IpAddress 58.211.1.12 \
    --Zone ap-guangzhou
```

Output: 
```
{
    "Response": {
        "CustomerGateway": {
            "CustomerGatewayId": "bmcgw-mgp33pll",
            "IpAddress": "58.211.1.12",
            "CustomerGatewayName": "test-cgw",
            "CreateTime": "2018-04-18 10:00:00"
        },
        "RequestId": "5bd98433-263a-47b6-9a1c-84aa613a8ff6"
    }
}
```

