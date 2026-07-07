**Example 1: 查询目标组列表**



Input: 

```
tccli alb DescribeTargetGroups --cli-unfold-argument  \
    --Filters.0.Name Protocol \
    --Filters.0.Values HTTP HTTPS \
    --MaxResults 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TargetGroups": [
            {
                "TargetGroupId": "lbtg-0zrnc9qa",
                "TargetGroupName": "group1",
                "TargetType": "Instance",
                "Protocol": "HTTP",
                "VpcId": "vpc-92hffaxb",
                "SchedulerAlgorithm": "wrr",
                "CreateTime": "2026-06-03T11:18:25+08:00",
                "KeepaliveEnabled": false,
                "Tags": [],
                "RelatedLoadBalancersCount": 2,
                "TargetGroupStatus": "Active",
                "HealthCheckConfig": {
                    "HealthCheckEnabled": true,
                    "HealthCheckPort": 0,
                    "HealthCheckProtocol": "HTTP",
                    "HealthCheckCodes": [
                        "http_1xx",
                        "http_2xx",
                        "http_3xx",
                        "http_4xx"
                    ],
                    "HealthCheckInterval": 5,
                    "HealthCheckHttpVersion": "HTTP1.1",
                    "HealthCheckMethod": "HEAD",
                    "HealthCheckPath": "/",
                    "HealthCheckTimeout": 2,
                    "HealthCheckHealthyThreshold": 3,
                    "HealthCheckUnhealthyThreshold": 3,
                    "HealthCheckHost": "aaa.com"
                },
                "StickySessionConfig": {
                    "StickySessionEnabled": false
                }
            },
            {
                "TargetGroupId": "lbtg-0zrnc9qa",
                "TargetGroupName": "group2",
                "TargetType": "Instance",
                "Protocol": "HTTP",
                "VpcId": "vpc-92hffaxb",
                "SchedulerAlgorithm": "wrr",
                "CreateTime": "2026-06-03T11:17:34+08:00",
                "KeepaliveEnabled": false,
                "Tags": [],
                "RelatedLoadBalancersCount": 0,
                "TargetGroupStatus": "Active",
                "HealthCheckConfig": {
                    "HealthCheckEnabled": true,
                    "HealthCheckPort": 0,
                    "HealthCheckProtocol": "HTTP",
                    "HealthCheckCodes": [
                        "http_1xx",
                        "http_2xx",
                        "http_3xx",
                        "http_4xx"
                    ],
                    "HealthCheckInterval": 5,
                    "HealthCheckHttpVersion": "HTTP1.1",
                    "HealthCheckMethod": "HEAD",
                    "HealthCheckPath": "/",
                    "HealthCheckTimeout": 2,
                    "HealthCheckHealthyThreshold": 3,
                    "HealthCheckUnhealthyThreshold": 3,
                    "HealthCheckHost": "aaa.com"
                },
                "StickySessionConfig": {
                    "StickySessionEnabled": false
                }
            }
        ],
        "RequestId": "fb47afdf-9728-4362-ad51-7049878fca3a"
    }
}
```

