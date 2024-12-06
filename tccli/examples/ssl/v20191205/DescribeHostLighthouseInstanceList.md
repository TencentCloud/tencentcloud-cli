**Example 1: lighthouse实例列表**

lighthouse实例列表

Input: 

```
tccli ssl DescribeHostLighthouseInstanceList --cli-unfold-argument  \
    --CertificateId heu**je \
    --IsCache 1 \
    --Filters.0.FilterKey domainMatch \
    --Filters.0.FilterValue 1 \
    --ResourceType lighthouse
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "InstanceId": "lhins-nh7lql34",
                "InstanceName": "个人网站",
                "IP": [
                    "124.221.178.108"
                ],
                "Domain": [
                    "7ui.cn",
                    "www.7ui.cn"
                ]
            }
        ],
        "RequestId": "d117a6c0-9a20-4d0e-917a-2f1599da3150"
    }
}
```

