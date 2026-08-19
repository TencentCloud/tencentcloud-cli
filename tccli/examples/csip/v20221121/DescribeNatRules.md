**Example 1: 获取NAT网关规则**



Input: 

```
tccli csip DescribeNatRules --cli-unfold-argument  \
    --AssetID nat*4*r*s**m \
    --MemberId mem-123
```

Output: 
```
{
    "Response": {
        "DnatRules": [
            {
                "Description": "",
                "IpProtocol": "TCP",
                "PrivateIpAddress": "1*2.**.4*.6",
                "PrivatePort": 666,
                "PublicIpAddress": "17*.1*8.15*.1*6",
                "PublicPort": 810
            }
        ],
        "SnatRules": [
            {
                "CreatedTime": "2023-10-16 18:17:58",
                "Description": "",
                "NatGatewaySnatId": "snat-88e*o**k",
                "PrivateIpAddress": "172.1*.*6.3*/*2",
                "PublicIpAddresses": "175.1*8.1*4.*06",
                "ResourceId": "",
                "ResourceType": "USERDEFINED"
            }
        ],
        "RequestId": "3dcf35ad-fa10-4d15-828a-0ff88333ca10"
    }
}
```

