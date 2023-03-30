**Example 1: 获取域名列表参数示例**

获取域名列表

Input: 

```
tccli dnspod DescribeDomainList --cli-unfold-argument  \
    --Type ALL \
    --Keyword dnspod \
    --Limit 1 \
    --Offset 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "DomainCountInfo": {
            "AllTotal": 35,
            "DomainTotal": 1,
            "ErrorTotal": 28,
            "GroupTotal": 0,
            "LockTotal": 1,
            "MineTotal": 28,
            "PauseTotal": 1,
            "ShareOutTotal": 4,
            "ShareTotal": 7,
            "SpamTotal": 0,
            "VipExpire": 0,
            "VipTotal": 4
        },
        "DomainList": [
            {
                "CNAMESpeedup": "DISABLE",
                "CreatedOn": "2021-05-06 20:40:39",
                "DNSStatus": "DNSERROR",
                "DomainId": 12614766,
                "EffectiveDNS": [
                    "ns3.dnsv5.com",
                    "ns4.dnsv5.com"
                ],
                "Grade": "DP_ULTRA",
                "GradeLevel": 10,
                "GradeTitle": "尊享版",
                "GroupId": 1,
                "IsVip": "YES",
                "Name": "dnspod.com",
                "Owner": "qcloud_uin_000000000@qcloud.com",
                "Punycode": "dnspod.com",
                "RecordCount": 0,
                "Remark": "",
                "SearchEnginePush": "NO",
                "Status": "ENABLE",
                "TTL": 600,
                "UpdatedOn": "2023-03-09 11:51:56",
                "VipAutoRenew": "YES",
                "VipEndAt": "2024-01-16 15:56:31",
                "VipStartAt": "2023-01-16 15:56:31"
            }
        ],
        "RequestId": "bfb3f27e-4dba-4a5c-9aff-08d1c27d1c61"
    }
}
```

