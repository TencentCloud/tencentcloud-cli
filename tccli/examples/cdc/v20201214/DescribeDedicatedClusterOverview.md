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
        "CvmCount": 36,
        "HostCount": 2,
        "VpnConnectionState": "AVAILABLE",
        "VpngwBandwidthData": {},
        "LocalNetInfo": {},
        "VpnConnectionBandwidthData": [],
        "RequestId": "ab5e5574-121b-4b5a-992c-fab691ac6737"
    }
}
```

