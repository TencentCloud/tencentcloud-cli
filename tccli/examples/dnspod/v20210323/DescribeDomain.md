**Example 1: 获取域名信息**

 

Input: 

```
tccli dnspod DescribeDomain --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "DomainInfo": {
            "DomainId": 1,
            "Status": "abc",
            "Grade": "abc",
            "GroupId": 1,
            "IsMark": "abc",
            "TTL": 1,
            "CnameSpeedup": "abc",
            "Remark": "abc",
            "Punycode": "abc",
            "DnsStatus": "abc",
            "DnspodNsList": [
                "abc"
            ],
            "Domain": "abc",
            "GradeLevel": 1,
            "UserId": 1,
            "IsVip": "abc",
            "Owner": "abc",
            "GradeTitle": "abc",
            "CreatedOn": "2020-09-22 00:00:00",
            "UpdatedOn": "2020-09-22 00:00:00",
            "Uin": "abc",
            "ActualNsList": [
                "abc"
            ],
            "RecordCount": 1,
            "OwnerNick": "abc",
            "IsGracePeriod": "abc",
            "VipBuffered": "abc",
            "VipStartAt": "abc",
            "VipEndAt": "abc",
            "VipAutoRenew": "abc",
            "VipResourceId": "abc",
            "IsSubDomain": true,
            "TagList": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

