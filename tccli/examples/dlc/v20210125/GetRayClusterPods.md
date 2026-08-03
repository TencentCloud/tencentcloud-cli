**Example 1: 获取集群的Pod列表**



Input: 

```
tccli dlc GetRayClusterPods --cli-unfold-argument  \
    --Id raycluster-20260527110617-96zt \
    --StartTime 1780112020000 \
    --EndTime 1780112020000 \
    --Page 1 \
    --PageSize 100
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CpuLimit": "1",
                "CpuRequest": "400m",
                "CreateTime": 1780112020000,
                "GpuCount": "0",
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
                "MemoryLimit": "4Gi",
                "MemoryRequest": "1.6Gi",
                "Namespace": "dlc-p-bleurqnv",
                "NodeIp": "30.0.0.31",
                "NodeName": "30.0.0.31",
                "Phase": "Running",
                "PodIp": "30.0.1.153",
                "PodName": "raycluster-20260527110617-96zt-head-6xn6r",
                "Role": "head",
                "StartTime": 1780112020000,
                "Status": "Running"
            }
        ],
        "Page": 1,
        "PageSize": 100,
        "Total": 2,
        "TotalPages": 1,
        "RequestId": "bdb54d51-8053-416f-836c-b682a798adee"
    }
}
```

