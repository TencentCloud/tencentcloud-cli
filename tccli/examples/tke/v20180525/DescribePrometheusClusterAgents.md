**Example 1: 拉取agent信息**



Input: 

```
tccli tke DescribePrometheusClusterAgents --cli-unfold-argument  \
    --InstanceId abc \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "ClusterType": "abc",
                "ClusterId": "abc",
                "Status": "abc",
                "ClusterName": "abc",
                "ExternalLabels": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "Region": "abc",
                "VpcId": "abc",
                "FailedReason": "abc"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

