**Example 1: 创建监听器转发规则**

创建HTTP/HTTPS监听器转发规则

Input: 

```
tccli gaap CreateRule --cli-unfold-argument  \
    --Domain www.bbb.com \
    --RealServerType IP \
    --HealthCheck 1 \
    --ListenerId listener-9jt0rtv9 \
    --CheckParams.ConnectTimeout 4 \
    --CheckParams.Path %2F \
    --CheckParams.Method HEAD \
    --CheckParams.DelayLoop 39 \
    --CheckParams.StatusCode 300 100 400 200 500 \
    --Scheduler rr \
    --Path %2Fimage
```

Output: 
```
{
    "Response": {
        "RequestId": "f3ab4984-dfe0-4c6f-aca0-32100550f6fd",
        "RuleId": "rule-qws4fmyl"
    }
}
```

