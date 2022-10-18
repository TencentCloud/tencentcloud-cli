**Example 1: 批量获取指定解析记录信息**



Input: 

```
tccli dnspod DescribeRecordListInfoBatch --cli-unfold-argument  \
    --RecordIdList 123123 412312
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
        ],
        "RecordList": [
            {
                "DomainId": "12615056",
                "RecordType": "URL",
                "TTL": "120",
                "Value": "http://www.baidu.com",
                "Status": "enable",
                "UpdatedOn": "2022-03-17 10:30:56",
                "LineId": "0",
                "Weight": "",
                "RecordId": "13763177",
                "Name": "baidu"
            },
            {
                "DomainId": "12615056",
                "RecordType": "CNAME",
                "TTL": "600",
                "Value": "baidu.com.",
                "Status": "enable",
                "UpdatedOn": "2022-04-13 14:20:31",
                "LineId": "0",
                "Weight": "20",
                "RecordId": "15678812",
                "Name": "cname"
            }
        ]
    }
}
```

