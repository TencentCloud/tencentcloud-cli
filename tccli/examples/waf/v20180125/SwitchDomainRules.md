**Example 1: 切换域名的规则开关**

切换域名的规则开关

Input: 

```
tccli waf SwitchDomainRules --cli-unfold-argument  \
    --Domain test.qcloudwaf.com \
    --Ids 1 2 3 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-efg"
    }
}
```

