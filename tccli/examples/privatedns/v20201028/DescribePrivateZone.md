**Example 1: 查询私有域详情**



Input: 

```
tccli privatedns DescribePrivateZone --cli-unfold-argument  \
    --ZoneId zone-p0152fh2
```

Output: 
```
{
    "Response": {
        "RequestId": "4b744f80-5061-4efa-b258-667316615200",
        "PrivateZone": {
            "ZoneId": "zone-p01g24h2",
            "OwnerUin": 100000123998,
            "Domain": "aarp",
            "CreatedOn": "2022-02-16 14:54:51",
            "UpdatedOn": "2022-02-16 20:12:22",
            "RecordCount": 2,
            "Remark": "",
            "VpcSet": [
                {
                    "UniqVpcId": "vpc-39kkc1s7",
                    "Region": "ap-guangzhou"
                }
            ],
            "AccountVpcSet": [],
            "Status": "ENABLED",
            "DnsForwardStatus": "DISABLED",
            "CnameSpeedupStatus": "DISABLED",
            "Tags": [],
            "IsCustomTld": false,
            "ForwardRuleName": "",
            "ForwardRuleType": "",
            "ForwardAddress": "",
            "EndPointName": ""
        }
    }
}
```

