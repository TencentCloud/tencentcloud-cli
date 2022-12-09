**Example 1: 查询私有域详情列表**



Input: 

```
tccli privatedns DescribePrivateZoneList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "a92efb27-74e6-462a-9b92-c836468eb111",
        "TotalCount": 22,
        "PrivateZoneSet": [
            {
                "ZoneId": "zone-e1g2senm",
                "OwnerUin": 100000123998,
                "Domain": "b.ac.cn",
                "CreatedOn": "2022-11-14 16:42:58",
                "UpdatedOn": "2022-11-14 16:42:59",
                "RecordCount": 0,
                "Remark": "tag",
                "VpcSet": [
                    {
                        "UniqVpcId": "vpc-39kkc543",
                        "Region": "ap-taipei"
                    }
                ],
                "AccountVpcSet": [],
                "Status": "ENABLED",
                "DnsForwardStatus": "ENABLED",
                "CnameSpeedupStatus": "ENABLED",
                "Tags": [],
                "IsCustomTld": false,
                "ForwardRuleName": "",
                "ForwardRuleType": "",
                "ForwardAddress": "",
                "EndPointName": ""
            }
        ]
    }
}
```

