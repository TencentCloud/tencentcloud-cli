**Example 1: 查询专用集群内宿主机的信息**

查询专用集群内宿主机的信息

Input: 

```
tccli cdc DescribeDedicatedClusterHostStatistics --cli-unfold-argument  \
    --DedicatedClusterId cluster-gbo27yc4
```

Output: 
```
{
    "Response": {
        "HostStatisticSet": [
            {
                "HostType": "S5.21XLARGE320",
                "HostFamily": "S5",
                "Cpu": 84,
                "Memory": 320,
                "Count": 240
            },
            {
                "HostType": "GN7.20XLARGE320",
                "HostFamily": "GN7",
                "Cpu": 80,
                "Memory": 320,
                "Count": 30
            },
            {
                "HostType": "M5.21XLARGE320",
                "HostFamily": "M5",
                "Cpu": 84,
                "Memory": 320,
                "Count": 128
            }
        ],
        "RequestId": "41aa48c2-477b-43c0-9d93-04ef3f529e5f"
    }
}
```

