**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveDomainCertBindings --cli-unfold-argument  \
    --CloudCertId hZy2N9vF \
    --DomainInfos.0.DomainName abc.tst.com.cn \
    --DomainInfos.0.Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cb91d382-e9be-4688-9008-d57088271b5f",
        "MismatchedDomainNames": [],
        "Errors": []
    }
}
```

