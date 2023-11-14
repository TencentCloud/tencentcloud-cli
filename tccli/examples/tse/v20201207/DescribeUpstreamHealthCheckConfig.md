**Example 1: demo**



Input: 

```
tccli tse DescribeUpstreamHealthCheckConfig --cli-unfold-argument  \
    --GatewayId abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnableActiveHealthCheck": true,
            "ActiveHealthCheck": {
                "HealthyInterval": 1,
                "UnHealthyInterval": 1,
                "HttpPath": "abc"
            },
            "EnablePassiveHealthCheck": true,
            "PassiveHealthCheck": {
                "Type": "abc"
            },
            "Successes": 1,
            "Failures": 1,
            "Timeouts": 1,
            "HealthyHttpStatuses": [
                1
            ],
            "UnhealthyHttpStatuses": [
                1
            ]
        },
        "RequestId": "abc"
    }
}
```

