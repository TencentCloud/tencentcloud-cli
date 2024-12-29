**Example 1: 修改转发规则信息**



Input: 

```
tccli gaap ModifyRuleAttribute --cli-unfold-argument  \
    --ListenerId listener-0s9kb7qt \
    --RuleId rule-o8aq26zj \
    --Path /path \
    --ForwardHost www.baidu.com \
    --ForcedRedirect  \
    --Scheduler rr \
    --HealthCheck 1 \
    --CheckParams.ConnectTimeout 2 \
    --CheckParams.DelayLoop 30 \
    --CheckParams.FailedThreshold 5 \
    --CheckParams.BlockInter 600 \
    --CheckParams.Path /path \
    --CheckParams.Method HEAD \
    --CheckParams.StatusCode 100 200 300 400 500 \
    --CheckParams.FailedCountInter 60 \
    --CheckParams.Domain www.baidu.com \
    --ServerNameIndicationSwitch ON \
    --ServerNameIndication www.baidu.com
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

