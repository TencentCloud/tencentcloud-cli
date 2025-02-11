**Example 1: 检查是否存在未开启waf代理设置但实际存在七层代理的域名**



Input: 

```
tccli waf DescribeUseCdnWithoutOpenProxyDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "RiskDomains": [
            {
                "Domain": "*.zhenhua125testwaf.com",
                "AccessType": "saaswaf domain",
                "Msg": "the domain use proxy services but do not set proxy on waf",
                "InstanceId": "waf_2kzfesre00ku283n"
            },
            {
                "Domain": "zhenhua1020.testwaf.com",
                "AccessType": "clbwaf domain",
                "Msg": "the domain use proxy services but do not set proxy on waf",
                "InstanceId": "waf_2kzfesre00ku07wh"
            }
        ],
        "Total": 2
    }
}
```

