**Example 1: 批量查询指定域名的详细信息**

批量查询指定域名的详细信息

Input: 

```
tccli dnspod DescribeDomainDetailListBatch --cli-unfold-argument  \
    --QcloudUin 100000014880 \
    --DomainList abc
```

Output: 
```
{
    "Response": {
        "DomainList": [
            {
                "DomainId": 1,
                "Name": "abc",
                "Status": "abc",
                "IsDNSPodNS": "abc",
                "Grade": "abc",
                "Punycode": "abc",
                "EffectiveDNS": [
                    "abc"
                ],
                "GradeTitle": "abc",
                "VipEndAt": "abc",
                "NowDNS": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

