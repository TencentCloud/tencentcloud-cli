**Example 1: GetLabPods**

获取实验室pods

Input: 

```
tccli dlc GetLabPods --cli-unfold-argument  \
    --Id raylab-20260530151529-r6av \
    --Page 1 \
    --PageSize 10 \
    --StartTime 1780125426000 \
    --EndTime 1780125426000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CpuLimit": "1",
                "CpuRequest": "400m",
                "CreateTime": 1780125426000,
                "GpuCount": "0",
                "Image": "ccr.ccs.tencentyun.com/emr-image/tcray:2.55.1-py311-cpu",
                "MemoryLimit": "4Gi",
                "MemoryRequest": "1.6Gi",
                "Namespace": "dlc-p-bleurqnv",
                "NodeIp": "30.0.0.30",
                "NodeName": "30.0.0.30",
                "Phase": "Running",
                "PodIp": "30.0.1.160",
                "PodName": "raylab-20260530151529-r6av-head-78mtl",
                "Role": "head",
                "StartTime": 1780125437000,
                "Status": "Running"
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 1,
        "TotalPages": 1,
        "RequestId": "e19b59a7-b73d-483b-850c-a1593bf43d35"
    }
}
```

