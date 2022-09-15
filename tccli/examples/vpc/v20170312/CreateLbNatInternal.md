**Example 1: demo**



Input: 

```
tccli vpc CreateLbNatInternal --cli-unfold-argument  \
    --AddLbNatSet.0.Owner 251197522 \
    --AddLbNatSet.0.LbVip 1.1.1.1 \
    --AddLbNatSet.0.VpcId 16769060 \
    --AddLbNatSet.0.Name test
```

Output: 
```
{
    "Response": {
        "AddLbNatResult": [
            {
                "VpcId": 16769060,
                "Name": "test",
                "UniqueVpcId": "vpc-7zayowkt",
                "UniqueLbNatId": "lbnat-j6xkxsqc",
                "CreateTime": "0000-00-00 00:00:00",
                "VpcOwnerLevel": -1,
                "OwnerLevel": -1,
                "Owner": "251197522",
                "GatewayIp": "9.198.109.113",
                "LbVip": "1.1.1.1",
                "LbNatId": 515,
                "GroupId": 0
            }
        ],
        "RequestId": "fb04215d-c669-48cb-a5f7-363b2063af02"
    }
}
```

