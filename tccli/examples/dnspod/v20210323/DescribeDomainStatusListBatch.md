**Example 1: 批量获取指定域名状态等信息**



Input: 

```
tccli dnspod DescribeDomainStatusListBatch --cli-unfold-argument  \
    --DomainIdList 123123 412312
```

Output: 
```
{
    "Response": {
        "RequestId": "66ddb097-ea5f-4b9c-a3aa-7dd044b6ab34",
        "DomainList": [
            {
                "Status": "enable",
                "IsDNSPodNS": "yes",
                "EffectiveDNS": [
                    "ns3.dnsv2.com",
                    "ns4.dnsv2.com"
                ],
                "NowDNS": [
                    "ns3.dnsv2.com",
                    "ns4.dnsv2.com"
                ],
                "GradeTitle": "专业版",
                "VipEndAt": "2025-01-06 13:11:48",
                "Name": "magicszhao.vip",
                "Punycode": "magicszhao.vip",
                "DomainId": "12615056"
            }
        ]
    }
}
```

