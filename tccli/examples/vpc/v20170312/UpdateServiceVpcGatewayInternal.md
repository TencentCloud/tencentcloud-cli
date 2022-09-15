**Example 1: demo**



Input: 

```
tccli vpc UpdateServiceVpcGatewayInternal --cli-unfold-argument  \
    --UpdateServiceVpcGatewaySet.0.Vip 10.19.0.186 \
    --UpdateServiceVpcGatewaySet.0.VpcId 1141 \
    --UpdateServiceVpcGatewaySet.0.VipVpcGatewayId vpcgw-fxu02n4l
```

Output: 
```
{
    "Response": {
        "UpdateServiceVpcGatewayResult": [
            {
                "VipVpcGatewayId": "vpcgw-fxu02n4l",
                "Vip": "10.19.0.186",
                "VpcId": 1141,
                "GroupId": 0,
                "HasUniqVpcGatewayIpVpcGatewayId": true
            }
        ],
        "RequestId": "cadfe7bf-01b0-40b6-9f51-8336de8957d7"
    }
}
```

