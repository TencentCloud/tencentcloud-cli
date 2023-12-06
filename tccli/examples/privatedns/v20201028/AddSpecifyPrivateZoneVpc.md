**Example 1: 追加与私有域关联的vpc**



Input: 

```
tccli privatedns AddSpecifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId abc \
    --VpcSet.0.UniqVpcId vpc-xxxxxxx \
    --VpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-xxxxxxxx \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.Uin 334345 \
    --AccountVpcSet.0.VpcName abc
```

Output: 
```
{
    "Response": {
        "ZoneId": "abc",
        "VpcSet": [
            {
                "UniqVpcId": "abc",
                "Region": "abc"
            }
        ],
        "AccountVpcSet": [
            {
                "Uin": "123456789",
                "UniqVpcId": "vpc-xxxxxxx",
                "Region": "ap-guangzhou"
            }
        ],
        "UniqId": "888888",
        "RequestId": "abc"
    }
}
```

