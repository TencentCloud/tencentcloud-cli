**Example 1: 追加与私有域关联的vpc**



Input: 

```
tccli privatedns AddSpecifyPrivateZoneVpc --cli-unfold-argument  \
    --ZoneId zone-dwuew12 \
    --VpcSet.0.UniqVpcId vpc-sd23d2 \
    --VpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-xxxxxxxx \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.Uin 334345 \
    --AccountVpcSet.0.VpcName vpc-testname
```

Output: 
```
{
    "Response": {
        "ZoneId": "zone-dwuew12",
        "VpcSet": [
            {
                "UniqVpcId": "vpc-sd23d2",
                "Region": "ap-guangzhou"
            }
        ],
        "AccountVpcSet": [
            {
                "Uin": "100000236200",
                "UniqVpcId": "vpc-dshgy2n",
                "Region": "ap-guangzhou",
                "VpcName": "vpc-testname"
            }
        ],
        "UniqId": "vpc-dser2gtg",
        "RequestId": "ba171d86-1337-48ca-a593-c8cbe46cdec5"
    }
}
```

