**Example 1: 专用集群概览信息**

专用集群概览信息

Input: 

```
tccli cdc DescribeDedicatedClusterOverview --cli-unfold-argument  \
    --DedicatedClusterId cluster-nk6e8j6c
```

Output: 
```
{
    "Response": {
        "CvmCount": 1,
        "HostCount": 1,
        "HostStandbyCount": 1,
        "HostNormalCount": 1,
        "VpnConnectionState": "abc",
        "VpngwBandwidthData": {
            "OutBandwidth": {
                "Timestamps": [
                    0
                ],
                "Values": [
                    0
                ]
            },
            "InBandwidth": {
                "Timestamps": [
                    0
                ],
                "Values": [
                    0
                ]
            }
        },
        "LocalNetInfo": {
            "Protocol": "abc",
            "VpcId": "abc",
            "BGPRoute": "abc",
            "LocalIp": "abc"
        },
        "VpnConnectionBandwidthData": [
            {
                "OutBandwidth": {
                    "Timestamps": [
                        0
                    ],
                    "Values": [
                        0
                    ]
                },
                "InBandwidth": {
                    "Timestamps": [
                        0
                    ],
                    "Values": [
                        0
                    ]
                }
            }
        ],
        "HostDetailInfo": [
            {
                "HostTypeFamily": "abc",
                "CpuTotal": 0,
                "CpuAvailable": 0,
                "MemTotal": 0,
                "MemAvailable": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

