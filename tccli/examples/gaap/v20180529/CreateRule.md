**Example 1: 创建监听器转发规则**

创建HTTP/HTTPS监听器转发规则

Input: 

```
tccli gaap CreateRule --cli-unfold-argument  \
    --RealServerType IP\
    --ListenerId listener-9jt0rtv9\
    --Scheduler rr\
    --Path %2Fimage\
    --CheckParams.StatusCode 100 200 300 400 500\
    --CheckParams.DelayLoop 39\
    --CheckParams.Path %2F\
    --CheckParams.Method HEAD\
    --CheckParams.ConnectTimeout 4\
    --Language zh-CN\
    --HealthCheck 1\
    --Domain www.bbb.com
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

