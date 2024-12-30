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
            "AllTotal": 27,
            "DomainTotal": 27,
            "ErrorTotal": 19,
            "GroupTotal": 0,
            "LockTotal": 0,
            "MineTotal": 20,
            "PauseTotal": 1,
            "ShareOutTotal": 4,
            "ShareTotal": 7,
            "SpamTotal": 3,
            "VipExpire": 0,
            "VipTotal": 6
        },
        "DomainList": [
            {
                "CNAMESpeedup": "DISABLE",
                "CreatedOn": "2023-03-21 17:27:40",
                "DNSStatus": "DNSERROR",
                "DomainId": 12620688,
                "EffectiveDNS": [
                    "temporary.dnspod.net",
                    "barman.dnspod.net"
                ],
                "Grade": "DP_FREE",
                "GradeLevel": 2,
                "GradeTitle": "免费版",
                "GroupId": 1,
                "IsVip": "NO",
                "Name": "dnspod.net",
                "Owner": "qcloud_uin_100000******@qcloud.com",
                "Punycode": "dnspod.net",
                "RecordCount": 182761,
                "Remark": "",
                "SearchEnginePush": "NO",
                "Status": "ENABLE",
                "TTL": 600,
                "TagList": [],
                "UpdatedOn": "2024-12-30 10:16:57",
                "VipAutoRenew": "NO",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipStartAt": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "789904fb-8dfc-445c-8467-3536ad88b237"
    }
}
```

