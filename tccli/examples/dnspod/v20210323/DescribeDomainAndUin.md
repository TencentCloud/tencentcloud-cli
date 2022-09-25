**Example 1: 获取域名信息及归属账号**



Input: 

```
tccli dnspod DescribeDomainAndUin --cli-unfold-argument  \
    --Domain dnspod.com
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "QcloudUin": "11111111111",
        "IsDNSPodNS": "yes",
        "EffectiveDNS": [
            "ns3.dnsv2.com",
            "ns4.dnsv2.com"
        ],
        "Status": "enable"
    }
}
```

