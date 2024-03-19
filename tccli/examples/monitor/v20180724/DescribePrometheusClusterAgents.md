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
                "FailedReason": "abc",
                "Name": "abc",
                "EnableExternal": true,
                "DesiredAgentNum": 0,
                "ReadyAgentNum": 0
            }
        ],
        "Total": 1,
        "IsFirstBind": true,
        "ImageNeedUpdate": true,
        "RequestId": "abc"
    }
}
```

