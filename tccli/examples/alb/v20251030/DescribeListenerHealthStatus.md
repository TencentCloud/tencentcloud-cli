**Example 1: 查询监听器健康状态**



Input: 

```
tccli alb DescribeListenerHealthStatus --cli-unfold-argument  \
    --IncludeRule False \
    --ListenerId lst-d9p3k7wa \
    --LoadBalancerId alb-f8q2xk9m \
    --MaxResults 20
```

Output: 
```
{
    "Response": {
        "ListenerId": "lst-d9p3k7wa",
        "ListenerPort": "80",
        "ListenerProtocol": "HTTP",
        "NextToken": "2c44874464923a9f",
        "RuleHealthStatusInfos": [
            {
                "IsDefaultRule": "false",
                "RuleId": "rule-h8cy5gwl",
                "TargetGroupHealthInfos": [
                    {
                        "HealthCheckEnabled": true,
                        "TargetGroupId": "lbtg-0zrnc9qa",
                        "TargetHealthStatusInfos": [
                            {
                                "Status": "Healthy",
                                "TargetId": "ins-x8q2m4pa",
                                "TargetIp": "10.0.0.1",
                                "TargetPort": 80
                            }
                        ],
                        "Type": "TargetGroup"
                    }
                ]
            }
        ],
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

