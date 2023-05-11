**Example 1: 删除域名规则白名单**

删除域名规则白名单

Input: 

```
tccli waf DeleteDomainWhiteRules --cli-unfold-argument  \
    --Domain abc.qcloudwaf.com \
    --Ids 111 222
```

Output: 
```
{
    "Response": {
        "RequestId": "46757c6e-786c-48ca-b5c4-9fa29ece1c9e",
        "Data": "abc"
    }
}
```

