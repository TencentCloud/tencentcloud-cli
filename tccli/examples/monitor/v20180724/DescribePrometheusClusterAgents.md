**Example 1: 拉取agent信息**

拉取agent信息

Input: 

```
tccli monitor DescribePrometheusClusterAgents --cli-unfold-argument  \
    --InstanceId abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "IsFirstBind": true,
        "Agents": [
            {
                "Status": "abc",
                "ClusterName": "abc",
                "ExternalLabels": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "ClusterId": "abc",
                "ClusterType": "abc",
                "Region": "abc",
                "VpcId": "abc",
                "FailedReason": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

