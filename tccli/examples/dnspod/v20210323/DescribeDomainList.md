**Example 1: 获取域名列表**



Input: 

```
tccli dnspod DescribeDomainList --cli-unfold-argument  \
    --Type ALL \
    --Keyword abc \
    --Limit 2 \
    --Offset 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "561cdfcb-37a6-47de-b3c5-2b038e2c2276",
        "DomainCountInfo": {
            "DomainTotal": 4,
            "AllTotal": 4,
            "MineTotal": 4,
            "ShareTotal": 0,
            "VipTotal": 1,
            "PauseTotal": 0,
            "ErrorTotal": 4,
            "LockTotal": 0,
            "SpamTotal": 0,
            "VipExpire": 0,
            "ShareOutTotal": 0,
            "GroupTotal": 3
        },
        "DomainList": [
            {
                "TTL": 600,
                "CNAMESpeedup": "DISABLE",
                "DNSStatus": "DNSERROR",
                "DomainId": 12609493,
                "Status": "ENABLE",
                "Grade": "DP_ULTRA",
                "GroupId": "1",
                "Remark": "",
                "CreatedOn": "2020-05-21 16:08:29",
                "UpdatedOn": "2021-04-01 18:09:58",
                "Punycode": "shenhailong.club",
                "Name": "shenhailong.club",
                "GradeLevel": 10,
                "GradeTitle": "企业旗舰版",
                "IsVip": "YES",
                "Owner": "qcloud_uin_100000012799@qcloud.com",
                "VipStartAt": "0000-00-00 00:00:00",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipAutoRenew": "NO",
                "SearchEnginePush": "NO",
                "RecordCount": 6,
                "EffectiveDNS": [
                    "ns3.dnsv5.com",
                    "ns4.dnsv5.com"
                ]
            },
            {
                "TTL": 600,
                "CNAMESpeedup": "DISABLE",
                "DNSStatus": "DNSERROR",
                "DomainId": 12610063,
                "Status": "ENABLE",
                "Grade": "DP_FREE",
                "GroupId": "1",
                "Remark": "",
                "CreatedOn": "2020-08-18 17:52:30",
                "UpdatedOn": "2020-08-18 17:52:30",
                "Punycode": "shenhailong.xn--fiqs8s",
                "Name": "shenhailong.中国",
                "GradeLevel": 2,
                "GradeTitle": "免费版",
                "IsVip": "NO",
                "Owner": "qcloud_uin_100000012799@qcloud.com",
                "VipStartAt": "0000-00-00 00:00:00",
                "VipEndAt": "0000-00-00 00:00:00",
                "VipAutoRenew": "NO",
                "SearchEnginePush": "NO",
                "RecordCount": 2,
                "EffectiveDNS": [
                    "f1g1ns1.dnspod.net",
                    "f1g1ns2.dnspod.net"
                ]
            }
        ]
    }
}
```

