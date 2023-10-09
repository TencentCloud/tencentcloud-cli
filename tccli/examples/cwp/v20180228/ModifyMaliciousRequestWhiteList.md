**Example 1: 更新恶意请求白名单**



Input: 

```
tccli cwp ModifyMaliciousRequestWhiteList --cli-unfold-argument  \
    --Id 1 \
    --Domain www.qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

