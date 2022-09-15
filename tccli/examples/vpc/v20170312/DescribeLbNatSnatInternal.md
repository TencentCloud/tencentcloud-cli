**Example 1: demo**



Input: 

```
tccli vpc DescribeLbNatSnatInternal --cli-unfold-argument  \
    --Owner 251197522 \
    --Limit 1 \
    --SnatIp 10.0.0.6
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "GetLbNatSnatResult": [
            {
                "VpcId": 16769060,
                "SameFlag": 0,
                "UniqueVpcId": "vpc-7zayowkt",
                "VpcGatewayIp": "0.0.0.0",
                "UniqueLbNatId": "lbnat-pbnqx1w2",
                "Owner": "251197522",
                "UniqueVpcGatewayId": "",
                "UniqueSubnetId": "subnet-1ufvulum",
                "SnatIp": "10.0.0.6",
                "SubnetId": 2007467,
                "LbNatId": 512,
                "CreateTime": "2022-07-04 15:47:16",
                "AutoApplyFlag": 1
            }
        ],
        "RequestId": "4aea4e3c-6e9e-4e13-98a4-957c05935943"
    }
}
```

