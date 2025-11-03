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
        "TotalCount": 25,
        "PodLimitsInstanceSet": [
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.12XLARGE96",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.LARGE8",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 27,
                    "TKERouteENIStaticIP": 27,
                    "TKEDirectENI": 19,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.12XLARGE128",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.2XLARGE32",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 95,
                    "TKERouteENIStaticIP": 95,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.LARGE16",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 27,
                    "TKERouteENIStaticIP": 27,
                    "TKEDirectENI": 19,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.2XLARGE16",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 95,
                    "TKERouteENIStaticIP": 95,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.4XLARGE64",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.40XLARGE320",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 22,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.MEDIUM4",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 27,
                    "TKERouteENIStaticIP": 27,
                    "TKEDirectENI": 9,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.16XLARGE128",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.20XLARGE160",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.8XLARGE64",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.SMALL1",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 5,
                    "TKERouteENIStaticIP": 5,
                    "TKEDirectENI": 4,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.32XLARGE256",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 22,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.SMALL4",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 5,
                    "TKERouteENIStaticIP": 5,
                    "TKEDirectENI": 4,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.16XLARGE256",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.MEDIUM2",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 27,
                    "TKERouteENIStaticIP": 27,
                    "TKEDirectENI": 9,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.22XLARGE192",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.16XLARGE192",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.MEDIUM8",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 27,
                    "TKERouteENIStaticIP": 27,
                    "TKEDirectENI": 9,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.22XLARGE224",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.4XLARGE32",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.4XLARGE16",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 273,
                    "TKERouteENIStaticIP": 273,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.2XLARGE8",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 95,
                    "TKERouteENIStaticIP": 95,
                    "TKEDirectENI": 39,
                    "TKESubENI": 100
                }
            },
            {
                "Zone": "ap-guangzhou-3",
                "InstanceFamily": "SA2",
                "InstanceType": "SA2.SMALL2",
                "PodLimits": {
                    "TKERouteENINonStaticIP": 5,
                    "TKERouteENIStaticIP": 5,
                    "TKEDirectENI": 4,
                    "TKESubENI": 100
                }
            }
        ],
        "RequestId": "0902e5fd-5b71-4ea7-b61b-1a281f7b48c6"
    }
}
```

