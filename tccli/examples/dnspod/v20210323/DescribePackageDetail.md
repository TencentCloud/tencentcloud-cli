**Example 1: 获取各套餐配置详情**

获取各套餐配置详情

Input: 

```
tccli dnspod DescribePackageDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "Info": [
            {
                "RealPrice": 0,
                "ChangedTimes": 0,
                "MinTtl": 120,
                "SubDomainLevel": 3,
                "MaxWildcard": 3,
                "DnsServerRegion": "8 个",
                "DomainGradeCn": "免费版",
                "GradeLevel": 1,
                "Ns": [
                    "s4g2m.dnspod.net",
                    "g8y9f.dnspod.net"
                ],
                "DomainGrade": "D_Free",
                "RecordRoll": 4
            },
            {
                "RealPrice": 698,
                "ChangedTimes": 0,
                "MinTtl": 1,
                "SubDomainLevel": 5,
                "MaxWildcard": 5,
                "DnsServerRegion": "10 个",
                "DomainGradeCn": "个人豪华版",
                "GradeLevel": 4,
                "Ns": [
                    "ns1.dnsv2.com",
                    "ns2.dnsv2.com"
                ],
                "DomainGrade": "D_Plus",
                "RecordRoll": 8
            },
            {
                "RealPrice": 588,
                "ChangedTimes": 0,
                "MinTtl": 60,
                "SubDomainLevel": 3,
                "MaxWildcard": 3,
                "DnsServerRegion": "12 个",
                "DomainGradeCn": "企业 I",
                "GradeLevel": 5,
                "Ns": [
                    "ns1.dnsv3.com",
                    "ns2.dnsv3.com"
                ],
                "DomainGrade": "D_Extra",
                "RecordRoll": 6
            },
            {
                "RealPrice": 1988,
                "ChangedTimes": 0,
                "MinTtl": 1,
                "SubDomainLevel": 8,
                "MaxWildcard": 8,
                "DnsServerRegion": "14 个",
                "DomainGradeCn": "企业 II",
                "GradeLevel": 7,
                "Ns": [
                    "ns1.dnsv4.com",
                    "ns2.dnsv4.com"
                ],
                "DomainGrade": "D_Expert",
                "RecordRoll": 10
            },
            {
                "RealPrice": 3688,
                "ChangedTimes": 0,
                "MinTtl": 1,
                "SubDomainLevel": 12,
                "MaxWildcard": 12,
                "DnsServerRegion": "16 个",
                "DomainGradeCn": "企业 III",
                "GradeLevel": 8,
                "Ns": [
                    "ns1.dnsv5.com",
                    "ns2.dnsv5.com"
                ],
                "DomainGrade": "D_Ultra",
                "RecordRoll": 99999
            },
            {
                "RealPrice": 0,
                "ChangedTimes": 0,
                "MinTtl": 600,
                "SubDomainLevel": 5,
                "MaxWildcard": 5,
                "DnsServerRegion": "8 个",
                "DomainGradeCn": "免费版",
                "GradeLevel": 2,
                "Ns": [
                    "s4g2m.dnspod.net",
                    "g8y9f.dnspod.net"
                ],
                "DomainGrade": "DP_Free",
                "RecordRoll": 2
            },
            {
                "RealPrice": 188,
                "ChangedTimes": 10,
                "MinTtl": 60,
                "SubDomainLevel": 20,
                "MaxWildcard": 20,
                "DnsServerRegion": "大于 12 个",
                "DomainGradeCn": "专业版",
                "GradeLevel": 3,
                "Ns": [
                    "ns3.dnsv2.com",
                    "ns4.dnsv2.com"
                ],
                "DomainGrade": "DP_Plus",
                "RecordRoll": 10
            },
            {
                "RealPrice": 1288,
                "ChangedTimes": 3,
                "MinTtl": 60,
                "SubDomainLevel": 8,
                "MaxWildcard": 8,
                "DnsServerRegion": "大于 14 个",
                "DomainGradeCn": "企业基础版",
                "GradeLevel": 6,
                "Ns": [
                    "ns3.dnsv3.com",
                    "ns4.dnsv3.com"
                ],
                "DomainGrade": "DP_Extra",
                "RecordRoll": 15
            },
            {
                "RealPrice": 2680,
                "ChangedTimes": 10,
                "MinTtl": 1,
                "SubDomainLevel": 30,
                "MaxWildcard": 30,
                "DnsServerRegion": "大于 16 个",
                "DomainGradeCn": "企业版",
                "GradeLevel": 9,
                "Ns": [
                    "ns3.dnsv4.com",
                    "ns4.dnsv4.com"
                ],
                "DomainGrade": "DP_Expert",
                "RecordRoll": 30
            },
            {
                "RealPrice": 29800,
                "ChangedTimes": 10,
                "MinTtl": 1,
                "SubDomainLevel": 999,
                "MaxWildcard": 999,
                "DnsServerRegion": "大于 20 个",
                "DomainGradeCn": "尊享版",
                "GradeLevel": 10,
                "Ns": [
                    "ns3.dnsv5.com",
                    "ns4.dnsv5.com"
                ],
                "DomainGrade": "DP_Ultra",
                "RecordRoll": 999
            },
            {
                "RealPrice": 29800,
                "ChangedTimes": 0,
                "MinTtl": 120,
                "SubDomainLevel": 8,
                "MaxWildcard": 8,
                "DnsServerRegion": "8 个",
                "DomainGradeCn": "DNSPod 体验版",
                "GradeLevel": 11,
                "Ns": [
                    "ns3.dnsv3.com",
                    "ns4.dnsv3.com"
                ],
                "DomainGrade": "DP_Local",
                "RecordRoll": 10
            }
        ],
        "LevelMap": [
            "D_Free",
            "DP_Free",
            "DP_Plus",
            "D_Plus",
            "D_Extra",
            "DP_Extra",
            "D_Expert",
            "D_Ultra",
            "DP_Expert",
            "DP_Ultra",
            "DP_Local"
        ]
    }
}
```

