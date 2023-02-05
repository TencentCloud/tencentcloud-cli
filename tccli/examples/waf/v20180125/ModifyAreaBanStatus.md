**Example 1: 设置域名的地域封禁状态**



Input: 

```
tccli waf ModifyAreaBanStatus --cli-unfold-argument  \
    --Domain test.qcloudwaf.com \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "8d630afc-0da8-43f6-862a-045e21ebfdba"
    }
}
```

