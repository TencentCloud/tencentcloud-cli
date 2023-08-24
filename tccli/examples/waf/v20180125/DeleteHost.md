**Example 1: 删除CLB-WAF防护域名**



Input: 

```
tccli waf DeleteHost --cli-unfold-argument  \
    --HostsDel ''[{"Domain":"lsd.qcloudwaf.com", "DomainId":"waf-MyBQKIZe"}]''
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

