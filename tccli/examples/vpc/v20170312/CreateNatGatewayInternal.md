**Example 1: 创建Nat内部实例**



Input: 

```
tccli vpc CreateNatGatewayInternal --cli-unfold-argument  \
    --NatGatewayName abc \
    --VpcId abc \
    --InternetMaxBandwidthOut 1 \
    --MaxConcurrentConnection 1 \
    --AddressCount 1 \
    --Zone abc \
    --Tags.0.Key abc \
    --Tags.0.Value abc
```

Output: 
```
{
    "Response": {
        "NatGatewaySet": [
            {
                "NatGatewayId": "abc",
                "NatGatewayName": "abc",
                "CreatedTime": "abc",
                "InternetMaxBandwidthOut": 1,
                "MaxConcurrentConnection": 1,
                "PublicIpAddressSet": [
                    {
                        "AddressId": "abc",
                        "PublicIpAddress": "abc",
                        "IsBlocked": true,
                        "BlockType": "abc"
                    }
                ],
                "NetworkState": "abc",
                "DestinationIpPortTranslationNatRuleSet": [
                    {
                        "IpProtocol": "abc",
                        "PublicIpAddress": "abc",
                        "PublicPort": 1,
                        "PrivateIpAddress": "abc",
                        "PrivatePort": 1,
                        "Description": "abc",
                        "CreatedTime": "2024-01-16 00:00:00"
                    }
                ],
                "VpcId": "abc",
                "Zone": "abc",
                "TagSet": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "GatewayType": "abc",
                "NatType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

