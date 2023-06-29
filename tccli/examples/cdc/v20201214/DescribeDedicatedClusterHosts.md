**Example 1: 专用集群宿主机信息**

专用集群宿主机信息

Input: 

```
tccli cdc DescribeDedicatedClusterHosts --cli-unfold-argument  \
    --DedicatedClusterId cluster-nk6e8j6c
```

Output: 
```
{
    "Response": {
        "HostInfoSet": [
            {
                "HostIp": "50.4.2.2",
                "ServiceType": "云服务器宿主机",
                "HostStatus": "PENDING",
                "HostType": "标准型S5.21XLARGE320",
                "RunTime": "2022-03-29 16:37:01",
                "ExpireTime": "2025-03-29 16:37:01",
                "CpuAvailable": 24,
                "CpuTotal": 24,
                "MemAvailable": 96,
                "MemTotal": 96
            },
            {
                "HostIp": "50.4.2.3",
                "ServiceType": "云服务器宿主机",
                "HostStatus": "PENDING",
                "HostType": "标准型S5.21XLARGE320",
                "RunTime": "2022-03-30 16:37:01",
                "ExpireTime": "2025-03-30 16:37:01",
                "CpuAvailable": 24,
                "CpuTotal": 24,
                "MemAvailable": 96,
                "MemTotal": 96
            }
        ],
        "TotalCount": 2,
        "RequestId": "7ffc723c-49d2-45ae-82cc-270aa35d3c59"
    }
}
```

