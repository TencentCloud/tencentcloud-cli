**Example 1: 拉取agent信息**

拉取agent信息

Input: 

```
tccli monitor DescribePrometheusClusterAgents --cli-unfold-argument  \
    --InstanceId prom-abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "ClusterId": "cls-abc",
                "ClusterName": "abc",
                "ClusterType": "tke",
                "EnableExternal": false,
                "ExternalLabels": [
                    {
                        "Name": "cluster",
                        "Value": "cls-cde"
                    },
                    {
                        "Name": "cluster_type",
                        "Value": "tke"
                    }
                ],
                "FailedReason": "",
                "Name": "",
                "ReadyAgentNum": 1,
                "Region": "ap-guangzhou",
                "Status": "normal",
                "VpcId": "vpc-abc"
            }
        ],
        "IsFirstBind": false,
        "RequestId": "56ce7-sdsd",
        "ImageNeedUpdate": false,
        "Total": 1
    }
}
```

