**Example 1: 获取作业的Pod列表**



Input: 

```
tccli dlc GetRayJobPods --cli-unfold-argument  \
    --Id rayjob-20260323163852-huvy \
    --Page 1 \
    --PageSize 10 \
    --StartTime 1771862400000 \
    --EndTime 1774454399000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CpuLimit": "1",
                "CpuRequest": "500m",
                "CreateTime": 1774255590000,
                "GpuCount": "0",
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:3.0.0.dev0-py311-cpu",
                "MemoryLimit": "1Gi",
                "MemoryRequest": "200Mi",
                "Namespace": "dlc-p-ofvhyjzn",
                "NodeIp": "169.254.128.2",
                "NodeName": "eklet-subnet-l8wxf43i-bd9cv4ef",
                "Phase": "Succeeded",
                "PodIp": "30.1.0.150",
                "PodName": "rayjob-20260323163852-huvy-8qd7h",
                "StartTime": 1774255660000,
                "Status": "Succeeded"
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 1,
        "TotalPages": 1,
        "RequestId": "53c77b8d-4a2b-4eef-957b-868d0e2b6ec5"
    }
}
```

