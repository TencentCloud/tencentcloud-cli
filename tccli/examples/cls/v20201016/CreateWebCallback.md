**Example 1: 创建告警渠道回调配置**

创建告警渠道回调配置

Input: 

```
tccli cls CreateWebCallback --cli-unfold-argument  \
    --Name name \
    --Type Http \
    --Webhook http://www.xxx.com \
    --Method POST \
    --Key 
```

Output: 
```
{
    "Response": {
        "WebCallbackId": "webcallback-aaa-bbb-ccc-ddd",
        "RequestId": "abc-abc-abc-abc"
    }
}
```

