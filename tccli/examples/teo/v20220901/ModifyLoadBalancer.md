**Example 1: 修改负载均衡实例的检查策略**

修改负载均衡实例的检查策略，调整为 HTTP 探测。

Input: 

```
tccli teo ModifyLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpaxol \
    --Name HTTP-LB \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId oog-30l3kv5z2bse \
    --OriginGroups.2.Priority priority_3 \
    --OriginGroups.2.OriginGroupId og-30l5kv5z22e9 \
    --HealthChecker.Type HTTP \
    --HealthChecker.Path www.qq.com/test111 \
    --HealthChecker.Port 80 \
    --HealthChecker.Interval 30 \
    --HealthChecker.Method HEAD \
    --HealthChecker.ExpectedCodes 200 400 401 402 403 404 405 406 408 409 410 411 412 413 414 415 416 417 418 421 423 424 426 429 431 433 434 444 451 499 \
    --HealthChecker.FollowRedirect false \
    --HealthChecker.Headers.0.Key header1 \
    --HealthChecker.Headers.0.Value header1 \
    --HealthChecker.Headers.1.Key header2 \
    --HealthChecker.Headers.1.Value header2 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherRecordInOriginGroup \
    --InstanceId lb-2sswjr6gnfy2
```

Output: 
```
{
    "Response": {
        "RequestId": "a66b1739-9f63-4c2b-bad2-8ef0ca714d56"
    }
}
```

