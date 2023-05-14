**Example 1: 创建对端网关**

创建对端网关

Input: 

```
tccli vpc CreateCustomerGateway --cli-unfold-argument  \
    --IpAddress 58.211.1.12 \
    --CustomerGatewayName test-cgw \
    --Tags.0.Value shanghai \
    --Tags.0.Key city
```

Output: 
```
{
    "Response": {
        "CustomerGateway": {
            "CustomerGatewayId": "cgw-mgp33pll",
            "IpAddress": "58.211.1.12",
            "CustomerGatewayName": "test-cgw",
            "CreatedTime": "2018-04-18 10:00:00"
        },
        "RequestId": "5bd98433-263a-47b6-9a1c-84aa613a8ff6"
    }
}
```

