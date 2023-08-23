**Example 1: 设置防护域名WAF开关**



Input: 

```
tccli waf ModifyHostStatus --cli-unfold-argument  \
    --HostsStatus ''[{"Domain":"lsd.qcloudwaf.com", "DomainId":"waf-MyBQKIZe", "Status":1}]''
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

