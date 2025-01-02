**Example 1: 创建告警渠道回调配置**

创建告警渠道回调配置

Input: 

```
tccli cls CreateWebCallback --cli-unfold-argument  \
    --Name 监控告警专用 \
    --Type WeCom \
    --Webhook http://www.xxx.com/send \
    --Method POST \
    --Key AADSHFYFNJKGYENGKVYDNGKFH<
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

