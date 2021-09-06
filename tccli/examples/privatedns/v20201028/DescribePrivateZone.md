**Example 1: 获取私有域**



Input: 

```
tccli privatedns DescribePrivateZone --cli-unfold-argument  \
    --ZoneId zone-123456
```

Output: 
```
{
    "Response": {
        "RequestId": "520fea07-9c1b-4560-1c8axxxx5275",
        "PrivateZone": {
            "ZoneId": "zone-123456",
            "OwnerUin": 1111111111111111,
            "Domain": "a.com",
            "CreatedOn": "2020-05-28 16:28:10",
            "UpdatedOn": "2020-11-18 00:11:59",
            "RecordCount": 10,
            "Remark": "测试域名",
            "VpcSet": [
                {
                    "UniqVpcId": "vpc-q1111115",
                    "Region": "ap-guangzhou"
                }
            ],
            "AccountVpcSet": [
                {
                    "UniqVpcId": "vpc-q1111115",
                    "Region": "ap-guangzhou",
                    "Uin": "123456789"
                }
            ],
            "Status": "ENABLED",
            "DnsForwardStatus": "DISABLED",
            "Tags": [
                {
                    "TagKey": "tagKey",
                    "TagValue": "tagValue"
                }
            ]
        }
    }
}
```

