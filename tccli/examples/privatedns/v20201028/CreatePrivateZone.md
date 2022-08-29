**Example 1: 创建私有域**



Input: 

```
tccli privatedns CreatePrivateZone --cli-unfold-argument  \
    --Domain a.com \
    --TagSet.0.TagKey owner \
    --TagSet.0.TagValue xxxxxxxxxx \
    --VpcSet.0.Region ap-guangzhou \
    --VpcSet.0.UniqVpcId vpc-xxxxxl \
    --AccountVpcSet.0.Uin 123456789 \
    --AccountVpcSet.0.Region ap-guangzhou \
    --AccountVpcSet.0.UniqVpcId vpc-adsebmy1 \
    --AccountVpcSet.0.VpcName vpcname \
    --Remark 测试域名 \
    --DnsForwardStatus ENABLED \
    --CnameSpeedupStatus ENABLED
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "ZoneId": "41",
        "Domain": "a.com"
    }
}
```

