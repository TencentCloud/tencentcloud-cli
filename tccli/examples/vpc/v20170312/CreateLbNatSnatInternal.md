**Example 1: demo**



Input: 

```
tccli vpc CreateLbNatSnatInternal --cli-unfold-argument  \
    --AddLbNatSnatSet.0.Owner 251197522 \
    --AddLbNatSnatSet.0.LbNatId 510 \
    --AddLbNatSnatSet.0.VpcId 16769060 \
    --AddLbNatSnatSet.0.SnatIp 10.0.0.17 \
    --AddLbNatSnatSet.0.UniqueSubnetId subnet-1ufvulum
```

Output: 
```
{
    "Response": {
        "AddLbNatSnatResult": [
            {
                "Subnet": "10.0.0.0",
                "VpcId": 16769060,
                "IntMask": 24,
                "UniqueVpcId": "vpc-7zayowkt",
                "UniqueLbNatId": "lbnat-1bymwtjo",
                "CreateTime": "0000-00-00 00:00:00",
                "SubnetId": 2007467,
                "UniqueSubnetId": "subnet-1ufvulum",
                "SnatIp": "10.0.0.17",
                "Owner": "251197522",
                "GatewayIp": "9.198.109.113",
                "LbVip": "10.0.123.11",
                "LbNatId": 510,
                "GroupId": 0,
                "SameFlag": 0
            }
        ],
        "RequestId": "bd4b1d98-da0e-4a6f-90b3-08ecc789b2a9"
    }
}
```

