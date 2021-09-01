**Example 1: 查询广州3区下的S5实例族机型可支持的 VPC-CNI Pod 数量**



Input: 

```
tccli tke DescribeVpcCniPodLimits --cli-unfold-argument  \
    --Zone ap-guangzhou-3, \
    --InstanceFamily S5,
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "PodLimitsInstanceSet": [
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "S5",
                "InstanceType": "S5.SMALL2",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 60,
                    "TKERouteENIStaticIP": 59,
                    "TKEDirectENI": 1
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "S5",
                "InstanceType": "S5.SMALL4",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 60,
                    "TKERouteENIStaticIP": 59,
                    "TKEDirectENI": 1
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "S5",
                "InstanceType": "S5.MEDIUM4",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 60,
                    "TKERouteENIStaticIP": 59,
                    "TKEDirectENI": 3
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "S5",
                "InstanceType": "S5.MEDIUM8",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 60,
                    "TKERouteENIStaticIP": 59,
                    "TKEDirectENI": 3
                }
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

