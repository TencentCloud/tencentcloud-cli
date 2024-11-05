**Example 1: 创建健康检查策略为 ICMP Ping 的负载均衡实例**

健康检查策略选择 ICMP Ping，请求重试策略选择重试组内其他源站。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpaxol \
    --Name ICMP-LB \
    --Type HTTP \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2bse \
    --HealthChecker.Type ICMP Ping \
    --HealthChecker.Interval 30 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherRecordInOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "c2967195-cfd7-4bd0-ac05-d2eaccde6909",
        "InstanceId": "lb-2osw7z07dnyu"
    }
}
```

**Example 2: 创建健康检查策略为 HTTPS 的负载均衡实例**

健康检查策略选择 HTTPS，请求重试策略选择重试组内其他源站。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpaxol \
    --Name HTTPS-LB \
    --Type GENERAL \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.2.Priority priority_3 \
    --OriginGroups.2.OriginGroupId og-30l5kv5z2bse \
    --HealthChecker.Type HTTPS \
    --HealthChecker.Path www.example.com/test \
    --HealthChecker.Port 80 \
    --HealthChecker.Interval 30 \
    --HealthChecker.Method HEAD \
    --HealthChecker.ExpectedCodes 200 500 501 502 503 504 505 507 520 521 525 530 544 562 567 599 \
    --HealthChecker.FollowRedirect true \
    --HealthChecker.Headers.0.Key header1 \
    --HealthChecker.Headers.0.Value header1 \
    --HealthChecker.Headers.1.Key header2 \
    --HealthChecker.Headers.1.Value header2 \
    --HealthChecker.Headers.2.Key header3 \
    --HealthChecker.Headers.2.Value header3 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherRecordInOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "c2967195-cfd7-4bd0-ac05-d2eaccde6909",
        "InstanceId": "lb-2osw7z17dnyu"
    }
}
```

**Example 3: 创建健康检查策略为 HTTP 的负载均衡实例**

健康检查策略选择 HTTP，请求重试策略选择重试组内其他源站。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpaxol \
    --Name HTTP-LB \
    --Type GENERAL \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.2.Priority priority_3 \
    --OriginGroups.2.OriginGroupId og-30l5kv5z2bse \
    --HealthChecker.Type HTTP \
    --HealthChecker.Path www.example.com/test \
    --HealthChecker.Port 80 \
    --HealthChecker.Interval 30 \
    --HealthChecker.Method HEAD \
    --HealthChecker.ExpectedCodes 200 500 501 502 503 504 505 507 520 521 525 530 544 562 567 599 \
    --HealthChecker.FollowRedirect true \
    --HealthChecker.Headers.0.Key header1 \
    --HealthChecker.Headers.0.Value header1 \
    --HealthChecker.Headers.1.Key header2 \
    --HealthChecker.Headers.1.Value header2 \
    --HealthChecker.Headers.2.Key header3 \
    --HealthChecker.Headers.2.Value header3 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherRecordInOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "c2967195-cfd7-4bd0-ac05-d2eaccde6909",
        "InstanceId": "lb-2osw7z07dnyu"
    }
}
```

**Example 4: 创建健康检查策略为 TCP 的负载均衡实例**

健康检查策略选择 TCP，请求重试策略选择重试下一优先级源站组。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnsaxol \
    --Name TCP-LB \
    --Type HTTP \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2bse \
    --HealthChecker.Type TCP \
    --HealthChecker.Port 80 \
    --HealthChecker.Interval 30 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "afe08af5-51f3-4f2e-911b-987ebb88a572",
        "InstanceId": "lb-2osbdyhu19iy"
    }
}
```

**Example 5: 创建健康检查策略为 UDP 的负载均衡实例**

健康检查策略选择 UDP，请求重试策略选择重试下一优先级源站组。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lsnpaxol \
    --Name UDP-LB \
    --Type GENERAL \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z215e \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2bse \
    --HealthChecker.Type UDP \
    --HealthChecker.Port 80 \
    --HealthChecker.SendContext requestcontent \
    --HealthChecker.RecvContext responsecontent \
    --HealthChecker.Interval 30 \
    --HealthChecker.Timeout 5 \
    --HealthChecker.HealthThreshold 3 \
    --HealthChecker.CriticalThreshold 2 \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "57d0154c-f9ab-42b7-ad83-232106647ff3",
        "InstanceId": "lb-2oswhs520uqe"
    }
}
```

**Example 6: 创建不启用探测的负载均衡实例**

不启用任何健康检查策略，请求重试策略选择重试下一优先级源站组。适用于仅配置主备源站的场景。

Input: 

```
tccli teo CreateLoadBalancer --cli-unfold-argument  \
    --ZoneId zone-2ju9lrnpaxol \
    --Name NoCheck-LB \
    --Type HTTP \
    --OriginGroups.0.Priority priority_1 \
    --OriginGroups.0.OriginGroupId og-30l5kv5z2bse \
    --OriginGroups.1.Priority priority_2 \
    --OriginGroups.1.OriginGroupId og-30l5kv5z2ase \
    --HealthChecker.Type NoCheck \
    --SteeringPolicy Pritory \
    --FailoverPolicy OtherOriginGroup
```

Output: 
```
{
    "Response": {
        "RequestId": "2c619f7f-27e9-43c5-b42c-68dcca803d35",
        "InstanceId": "lb-2osw2ssziowm"
    }
}
```

