**Example 1: 获取域名筛选列表参数示例**

获取域名筛选列表

Input: 

```
tccli dnspod DescribeDomainFilterList --cli-unfold-argument  \
    --Type ALL \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "DomainCountInfo": {
            "DomainTotal": 1,
            "AllTotal": 1,
            "MineTotal": 1,
            "ShareTotal": 1,
            "VipTotal": 1,
            "PauseTotal": 1,
            "ErrorTotal": 1,
            "LockTotal": 1,
            "SpamTotal": 1,
            "VipExpire": 1,
            "ShareOutTotal": 1,
            "GroupTotal": 1
        },
        "DomainList": [
            {
                "DomainId": 1,
                "Name": "abc",
                "Status": "abc",
                "TTL": 1,
                "CNAMESpeedup": "abc",
                "DNSStatus": "abc",
                "Grade": "abc",
                "GroupId": 1,
                "SearchEnginePush": "abc",
                "Remark": "abc",
                "Punycode": "abc",
                "EffectiveDNS": [
                    "abc"
                ],
                "GradeLevel": 1,
                "GradeTitle": "abc",
                "IsVip": "abc",
                "VipStartAt": "2020-09-22 00:00:00",
                "VipEndAt": "2020-09-22 00:00:00",
                "VipAutoRenew": "abc",
                "RecordCount": 1,
                "CreatedOn": "2020-09-22 00:00:00",
                "UpdatedOn": "2020-09-22 00:00:00",
                "Owner": "abc",
                "TagList": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

