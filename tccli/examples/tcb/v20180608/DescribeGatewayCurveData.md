**Example 1: 查询网关监控数据实例**

查询网关监控数据实例

Input: 

```
tccli tcb DescribeGatewayCurveData --cli-unfold-argument  \
    --EnvId envId \
    --GatewayId gatewayId \
    --GatewayVersion version-001 \
    --GatewayRoute route \
    --MetricName GwHttp404 \
    --StartTime 2022-02-22 20:08:10 \
    --EndTime 2022-02-22 20:18:10
```

Output: 
```
{
    "Response": {
        "Period": 1,
        "Values": [
            0,
            0
        ],
        "RequestId": "req",
        "StartTime": "2022-02-22 20:08:10",
        "Time": [
            1640845840,
            1640845841
        ],
        "EndTime": "2022-02-22 20:18:10",
        "MetricName": "GwHttp404"
    }
}
```

