**Example 1: demo**



Input: 

```
tccli vpc DeleteLbNatSnatInternal --cli-unfold-argument  \
    --DelLbNatSnatSet.0.SubnetId 2007467 \
    --DelLbNatSnatSet.0.Owner 251197522 \
    --DelLbNatSnatSet.0.VpcId 16769060 \
    --DelLbNatSnatSet.0.SnatIp 10.0.0.17 \
    --DelLbNatSnatSet.0.LbNatId 510
```

Output: 
```
{
    "Response": {
        "DelLbNatSnatResult": [
            {
                "VpcId": 16769060,
                "UniqueVpcId": "vpc-7zayowkt",
                "UniqueLbNatId": "lbnat-1bymwtjo",
                "SubnetId": 2007467,
                "SnatIp": "10.0.0.17",
                "Owner": "251197522",
                "GatewayIp": "9.198.109.113",
                "LbVip": "10.0.123.11",
                "LbNatId": 510,
                "GroupId": 0
            }
        ],
        "RequestId": "e905e482-424f-4340-9513-3d8ce064529e"
    }
}
```

