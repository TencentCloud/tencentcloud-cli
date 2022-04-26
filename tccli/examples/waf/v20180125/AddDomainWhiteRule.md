**Example 1: 增加域名规则白名单**



Input: 

```
tccli waf AddDomainWhiteRule --cli-unfold-argument  \
    --Domain abc.qcloudwaf.com \
    --Rules 2 \
    --Url /aa \
    --Function prefix \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "cdf",
        "Id": 111
    }
}
```

