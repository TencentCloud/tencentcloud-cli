**Example 1: 获取发现域名列表接口**



Input: 

```
tccli waf DescribeFindDomainList --cli-unfold-argument  \
    --Offset 2 \
    --Limit 5 \
    --Key qcloudwaf.com \
    --IsWafDomain 1
```

Output: 
```
{
    "Response": {
        "Total": 9,
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "List": [
            {
                "Appid": 251000001,
                "Domain": "lucasssli3.qcloudwaf.com",
                "Ips": [
                    "159.75.189.237"
                ],
                "FindTime": "20210729",
                "InstanceId": "waf_0000000001",
                "DomainId": "waf-oV8zE3WP",
                "Edition": "clb-waf",
                "IsWafDomain": 1
            },
            {
                "Appid": 251000001,
                "Domain": "wwwtx.qcloudwaf.com",
                "Ips": [
                    "159.75.189.237"
                ],
                "FindTime": "20210730",
                "InstanceId": "waf_2kuil2fm02vqm7t5",
                "DomainId": "waf-KsC0pPCo",
                "Edition": "clb-waf",
                "IsWafDomain": 1
            },
            {
                "Appid": 251000001,
                "Domain": "0613.qcloudwaf.com",
                "Ips": [
                    "119.29.47.251"
                ],
                "FindTime": "20210730",
                "InstanceId": "waf_2kuil2fm02vqm7t5",
                "DomainId": "waf_mfhvyos1",
                "Edition": "clb-waf",
                "IsWafDomain": 0
            },
            {
                "Appid": 251000001,
                "Domain": "txwaf.qcluodwaf.com",
                "Ips": [
                    "159.75.189.237"
                ],
                "FindTime": "20210730",
                "InstanceId": "waf_2kuil2fm02fsdm1",
                "DomainId": "waf_vlsdf123m",
                "Edition": "sparta-waf",
                "IsWafDomain": 0
            }
        ]
    }
}
```

