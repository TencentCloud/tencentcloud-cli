**Example 1: 拉取agent信息**

拉取agent信息

Input: 

```
tccli tke DescribePrometheusAgents --cli-unfold-argument  \
    --InstanceId prom-dsgfjhv \
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
                "Status": "running",
                "ClusterName": "北京测试集群",
                "ClusterId": "cls-dhsjffg",
                "ClusterType": "tke",
                "ExternalLabels": [
                    {
                        "Name": "cluster",
                        "Value": "cls-dhsjffg"
                    }
                ],
                "Region": "ap-beijing",
                "VpcId": "vpc-dsahjggf",
                "FailedReason": ""
            }
        ],
        "RequestId": "f1de3153-88df-45c2-9f39-cddjkiiug234897h"
    }
}
```

