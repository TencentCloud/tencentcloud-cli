**Example 1: 查询容灾站点VPC映射**



Input: 

```
tccli bdrc DescribeVpcMappings --cli-unfold-argument  \
    --SitePairId sitepair-0wxbktxr
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpcMappingSet": [
            {
                "Id": 106,
                "LifeState": "NORMAL",
                "SitePairId": "sitepair-0wxbktxr",
                "SourceSubnet": "subnet-9pqg3i8o",
                "SourceVpc": "vpc-i9pwklpn",
                "Status": "",
                "TargetSubnet": "subnet-kw0s0e5u",
                "TargetVpc": "vpc-ap4fkwyt"
            }
        ],
        "RequestId": "b450cce0-7254-46e1-baeb-05a974f67c3b"
    }
}
```

