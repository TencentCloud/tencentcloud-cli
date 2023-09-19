**Example 1: 删除私有域关联的VPC**



Input: 

```
tccli privatedns DeleteSpecifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId abc \
    --VpcSet.0.UniqVpcId vpc-xxxxxxxx \
    --VpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-xxxxxxxx \
    --AccountVpcSet.0.Region ap-gangzhou \
    --AccountVpcSet.0.Uin 888774747 \
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
        "RequestId": "abc"
    }
}
```

