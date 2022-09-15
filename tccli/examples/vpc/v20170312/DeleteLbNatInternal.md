**Example 1: demo**



Input: 

```
tccli vpc DeleteLbNatInternal --cli-unfold-argument  \
    --DelLbNatSet.0.Owner 251197522 \
    --DelLbNatSet.0.LbNatId 514 \
    --DelLbNatSet.0.UniqueLbNatId lbnat-9d8ubjkq \
    --DelLbNatSet.0.VpcId 16769060
```

Output: 
```
{
    "Response": {
        "DelLbNatResult": [
            {
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "GwRelayFlag": 0,
                "UniqueLbNatId": "lbnat-9d8ubjkq",
                "ToaFlag": 1,
                "Owner": "251197522",
                "GatewayIp": "9.198.109.113",
                "GroupId": 0,
                "Name": "test",
                "CreateTime": "2022-09-06 15:35:19",
                "ZoneId": 0,
                "AutoLearningFlag": 0,
                "State": 0,
                "VpcOwnerLevel": -1,
                "OwnerLevel": -1,
                "LbVip": "1.1.1.1",
                "LbNatId": 514
            }
        ],
        "RequestId": "9c2c86da-9b06-4ff2-bd9d-e43d667a702d"
    }
}
```

