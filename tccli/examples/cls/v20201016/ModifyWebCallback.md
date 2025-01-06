**Example 1: 修改告警渠道回调配置**

修改告警渠道回调配置

Input: 

```
tccli cls ModifyWebCallback --cli-unfold-argument  \
    --WebCallbackId webcallback-d20a21f7-xxxx-xxxx-ba1b-1aa49be5fed1 \
    --Name 监控告警专用 \
    --Type Http \
    --Webhook http://www.xxx.com \
    --Method POST \
    --Key HHFNIKFKLAUPOISNFIUYIOIA
```

Output: 
```
{
    "Response": {
        "RequestId": "d20a21f7-xxxx-xxxx-ba1b-1aa49be5fed1"
    }
}
```

