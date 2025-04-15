**Example 1: 修改私有域关联的VPC**



Input: 

```
tccli privatedns ModifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId zone-12345ds6 \
    --VpcSet.0.Region ap-guangzhou \
    --VpcSet.0.UniqVpcId vpc-xxxxxx \
    --AccountVpcSet.0.Uin 1002450010 \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-dsd8ulf \
    --AccountVpcSet.0.VpcName vpcName
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "ZoneId": "zone-12345ds6",
        "VpcSet": [
            {
                "UniqVpcId": "vpc-dsd8ulf",
                "Region": "ap-guangzhou"
            }
        ],
        "AccountVpcSet": [
            {
                "Uin": "1002450010",
                "UniqVpcId": "vpc-dsd8sdw",
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

