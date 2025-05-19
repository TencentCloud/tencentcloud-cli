**Example 1: 删除私有域关联的VPC**



Input: 

```
tccli privatedns DeleteSpecifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId zone-sdasd12d \
    --VpcSet.0.UniqVpcId vpc-dae2312 \
    --VpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-2314dae \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.Uin 1000032110 \
    --AccountVpcSet.0.VpcName vpc-testname
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-sdasd12d",
        "VpcSet": [
            {
                "UniqVpcId": "vpc-dae2312",
                "Region": "ap-guangzhou"
            }
        ],
        "AccountVpcSet": [
            {
                "Uin": "1000032110",
                "UniqVpcId": "vpc-2314dae",
                "Region": "ap-guangzhou",
                "VpcName": "vpc-testname"
            }
        ],
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845"
    }
}
```

