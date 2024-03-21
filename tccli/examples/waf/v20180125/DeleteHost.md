**Example 1: 删除负载均衡型WAF防护域名**



Input: 

```
tccli waf DeleteHost --cli-unfold-argument  \
    --HostsDel.0.Domain test.clb.qcloud.com \
    --HostsDel.0.DomainId waf-n7GFuVNJ \
    --HostsDel.0.InstanceID waf_2kuil2fm02vqm7z3
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

