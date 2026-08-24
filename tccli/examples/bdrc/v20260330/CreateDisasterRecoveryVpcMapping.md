**Example 1: 创建VPC映射**



Input: 

```
tccli bdrc CreateDisasterRecoveryVpcMapping --cli-unfold-argument  \
    --SourceVpcId vpc-i9pwklpn \
    --SourceSubnetId subnet-9pqg3i8o \
    --TargetVpcId vpc-ap4fkwyt \
    --TargetSubnetId subnet-kw0s0e5u \
    --SitePairId sitepair-3k23fkmn
```

Output: 
```
{
    "Response": {
        "RequestId": "d844f18d-aaad-4e45-b20f-92e1b7023a74"
    }
}
```

