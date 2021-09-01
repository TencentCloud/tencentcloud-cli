**Example 1: 删除路由规则**



Input: 

```
tccli vpc DeleteRoutes --cli-unfold-argument  \
    --Routes.0.DestinationCidrBlock 10.0.0.0/16 \
    --Routes.0.Enabled True \
    --Routes.0.RouteId 364153 \
    --Routes.0.GatewayType EIP \
    --Routes.0.GatewayId vpc-b1qdfp5v \
    --RouteTableId rtb-m1xkaxvq
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "DestinationCidrBlock": "10.0.0.0/16",
                "RouteTableId": "rtb-m1xkaxvq",
                "GatewayType": "EIP",
                "GatewayId": "vpc-b1qdfp5v",
                "DestinationIpv6CidrBlock": "xx"
            }
        ],
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

