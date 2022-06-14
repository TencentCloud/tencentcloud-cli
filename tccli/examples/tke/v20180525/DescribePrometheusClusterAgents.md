**Example 1: 拉取agent信息**



Input: 

```
tccli tke DescribePrometheusClusterAgents --cli-unfold-argument  \
    --InstanceId xx \
    --Limit 1 \
    --Offset 1
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
                "ExternalLabels": [
                    {
                        "Name": "xx",
                        "Value": "xx"
                    }
                ],
                "ClusterId": "xx",
                "ClusterType": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

