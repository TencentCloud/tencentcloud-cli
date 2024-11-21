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
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

