**Example 1: 拉取agent信息**



Input: 

```
tccli tke DescribePrometheusAgents --cli-unfold-argument  \
    --InstanceId prom-xxxxxx \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Agents": [
            {
                "Status": "xx",
                "ClusterName": "xx",
                "ClusterId": "xx",
                "ClusterType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

