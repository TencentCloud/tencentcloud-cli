**Example 1: 设置防护域名WAF开关**



Input: 

```
tccli waf ModifyHostStatus --cli-unfold-argument  \
    --HostsStatus.0.Status 1 \
    --HostsStatus.0.Domain evantt.qcloudwaf.com \
    --HostsStatus.0.DomainId waf-cblsyzU7 \
    --HostsStatus.0.InstanceID waf_2kuil2fm02vqm7z3
```

Output: 
```
{
    "Response": {
        "Success": {
            "Code": "Success",
            "Message": "Success"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

