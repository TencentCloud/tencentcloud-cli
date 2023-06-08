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
            "AllTotal": 41,
            "DomainTotal": 41,
            "ErrorTotal": 34,
            "GroupTotal": 0,
            "LockTotal": 0,
            "MineTotal": 34,
            "PauseTotal": 1,
            "ShareOutTotal": 3,
            "ShareTotal": 7,
            "SpamTotal": 0,
            "VipExpire": 0,
            "VipTotal": 3
        },
        "DomainList": [
            {
                "CNAMESpeedup": "DISABLE",
                "CreatedOn": "2023-01-29 16:59:00",
                "DNSStatus": "DNSERROR",
                "DomainId": 12620610,
                "EffectiveDNS": [
                    "v4u4f.dnspod.net",
                    "h9w2s.dnspod.net"
                ],
                "Grade": "DP_FREE",
                "GradeLevel": 2,
                "GradeTitle": "免费版",
                "GroupId": 1,
                "IsVip": "NO",
                "Name": "dnspod.com",
                "Owner": "qcloud_uin_1000000xxxx@qcloud.com",
                "Punycode": "dnspod.com",
                "RecordCount": 0,
                "Remark": "",
                "SearchEnginePush": "NO",
                "Status": "ENABLE",
                "TTL": 600,
                "UpdatedOn": "2023-01-29 16:59:00",
                "VipAutoRenew": "NO",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipStartAt": "0000-00-00 00:00:00"
            },
            {
                "CNAMESpeedup": "DISABLE",
                "CreatedOn": "2023-01-29 11:53:20",
                "DNSStatus": "DNSERROR",
                "DomainId": 12620607,
                "EffectiveDNS": [
                    "v4u4f.dnspod.net",
                    "h9w2s.dnspod.net"
                ],
                "Grade": "DP_FREE",
                "GradeLevel": 2,
                "GradeTitle": "免费版",
                "GroupId": 1,
                "IsVip": "NO",
                "Name": "dnspod1111.com",
                "Owner": "qcloud_uin_1000000xxxx@qcloud.com",
                "Punycode": "dnspod1111.com",
                "RecordCount": 0,
                "Remark": "",
                "SearchEnginePush": "NO",
                "Status": "ENABLE",
                "TTL": 600,
                "UpdatedOn": "2023-01-29 11:53:20",
                "VipAutoRenew": "NO",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipStartAt": "0000-00-00 00:00:00"
            },
            {
                "CNAMESpeedup": "DISABLE",
                "CreatedOn": "2022-12-16 14:48:49",
                "DNSStatus": "DNSERROR",
                "DomainId": 12620584,
                "EffectiveDNS": [
                    "v4u4f.dnspod.net",
                    "h9w2s.dnspod.net"
                ],
                "Grade": "DP_FREE",
                "GradeLevel": 2,
                "GradeTitle": "免费版",
                "GroupId": 1,
                "IsVip": "NO",
                "Name": "dnspod22222.com",
                "Owner": "qcloud_uin_1000000xxxx@qcloud.com",
                "Punycode": "dnspod22222.com",
                "RecordCount": 0,
                "Remark": "",
                "SearchEnginePush": "NO",
                "Status": "ENABLE",
                "TTL": 600,
                "UpdatedOn": "2022-12-16 14:48:49",
                "VipAutoRenew": "NO",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipStartAt": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "c1e2fbcf-fbf4-4cc8-a59a-dddedcc8a59e"
    }
}
```

