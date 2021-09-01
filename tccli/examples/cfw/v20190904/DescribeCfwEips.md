**Example 1: 查询防火墙弹性公网ip**



Input: 

```
tccli cfw DescribeCfwEips --cli-unfold-argument  \
    --Mode 1 \
    --NatGatewayId ALL \
    --CfwInstance cfwnat-d2afc817
```

Output: 
```
{
    "Response": {
        "NatFwEipList": [
            {
                "Eip": "xxx",
                "NatGatewayId": "nat-xxx",
                "NatGatewayName": "xxx"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

