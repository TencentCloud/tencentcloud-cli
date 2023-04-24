**Example 1: 修改一条转发规则的健康检查参数及转发策略**

修改一条转发规则的健康检查参数及转发策略。

Input: 

```
tccli clb ModifyRule --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-4fbxq45k \
    --LocationId loc-9dr7bsl3 \
    --Url /bar \
    --Scheduler LEAST_CONN \
    --SessionExpireTime 75 \
    --HealthCheck.HealthSwitch 1 \
    --HealthCheck.IntervalTime 50 \
    --HealthCheck.HealthNum 3 \
    --HealthCheck.UnHealthNum 3 \
    --HealthCheck.HttpCode 7 \
    --HealthCheck.HttpCheckPath /check \
    --HealthCheck.HttpCheckDomain foo.net \
    --HealthCheck.HttpCheckMethod GET
```

Output: 
```
{
    "Response": {
        "RequestId": "6d846dfd-27f3-4d74-bc00-ec9ae0570cb0"
    }
}
```

