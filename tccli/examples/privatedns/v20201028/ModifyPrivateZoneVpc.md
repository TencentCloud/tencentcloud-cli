**Example 1: 修改私有域关联的VPC**



Input: 

```
tccli privatedns ModifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId 1 \
    --VpcSet.0.Region ap-guangzhou \
    --VpcSet.0.UniqVpcId vpc-xxxxxx \
    --AccountVpcSet.0.Uin 123456789 \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-xxxxxx \
    --AccountVpcSet.0.VpcName vpcName
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "ZoneId": "1",
        "VpcSet": [
            {
                "UniqVpcId": "vpc-xxxxxxx",
                "Region": "ap-guangzhou"
            }
        ],
        "AccountVpcSet": [
            {
                "Uin": "123456789",
                "UniqVpcId": "vpc-xxxxxxx",
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

