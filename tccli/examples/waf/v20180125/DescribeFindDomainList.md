**Example 1: 获取发现域名列表接口**



Input: 

```
tccli waf DescribeFindDomainList --cli-unfold-argument  \
    --Offset 2 \
    --Limit 5 \
    --Key  \
    --IsWafDomain 
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
                "Domain": "lucasssli3.qcloud.com",
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
                "Domain": "www.atestwaf1.com",
                "Ips": [
                    "159.75.189.237"
                ],
                "FindTime": "20210730",
                "InstanceId": "",
                "DomainId": "waf-KsC0pPCo",
                "Edition": "clb-waf",
                "IsWafDomain": 1
            },
            {
                "Appid": 251000001,
                "Domain": "0613.1314zf.com",
                "Ips": [
                    "119.29.47.251"
                ],
                "FindTime": "20210730",
                "InstanceId": "",
                "DomainId": "",
                "Edition": "",
                "IsWafDomain": 0
            },
            {
                "Appid": 251000001,
                "Domain": "www.atestwaf1.com",
                "Ips": [
                    "159.75.189.237"
                ],
                "FindTime": "20210730",
                "InstanceId": "",
                "DomainId": "",
                "Edition": "",
                "IsWafDomain": 0
            }
        ]
    }
}
```

