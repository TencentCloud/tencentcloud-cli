**Example 1: 修改告警渠道回调配置**

修改告警渠道回调配置

Input: 

```
tccli cls ModifyWebCallback --cli-unfold-argument  \
    --WebCallbackId webcallback-d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1 \
    --Name name \
    --Type Http \
    --Webhook http://www.xxx.com \
    --Method POS \
    --Key d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1
```

Output: 
```
{
    "Response": {
        "RequestId": "d20a21f7-f6ac-4a7b-ba1b-1aa49be5fed1"
    }
}
```

