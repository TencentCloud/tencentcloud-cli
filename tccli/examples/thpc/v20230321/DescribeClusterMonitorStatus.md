**Example 1: 查询集群的监控状态**



Input: 

```
tccli thpc DescribeClusterMonitorStatus --cli-unfold-argument  \
    --ClusterId hpc-********
```

Output: 
```
{
    "Response": {
        "MonitorStatus": "DISABLED",
        "PrometheusId": "prom-********",
        "RequestId": "1b1ba87a-0565-4b48-bea1-5f85ee921abb"
    }
}
```

