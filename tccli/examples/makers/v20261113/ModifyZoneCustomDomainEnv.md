**Example 1: 修改自定义域名环境**



Input: 

```
tccli makers ModifyZoneCustomDomainEnv --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --Domain ************************ \
    --Env Preview
```

Output: 
```
{
    "Response": {
        "Domain": "************************",
        "Env": "Preview",
        "RequestId": "bb2a6c27-e2f8-436f-ab46-c0fddb4cb85b"
    }
}
```

