**Example 1: 修改域名列表的访问日志开关**



Input: 

```
tccli waf ModifyDomainsCLSStatus --cli-unfold-argument  \
    --Domains.0.Domain lucasssli1.qcloud.com \
    --Domains.0.Edition clb-waf \
    --Domains.1.Domain lucasssli2.qcloud.com \
    --Domains.1.Edition clb-waf \
    --Domains.2.Domain lucasssli3.qcloud.com \
    --Domains.2.Edition sparta-waf \
    --Domains.3.Domain lucasssli4.qcloud.com \
    --Domains.3.Edition sparta-waf \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2"
    }
}
```

