**Example 1: pod列表**

获取任务对应的pod列表

Input: 

```
tccli tione DescribeTrainingTaskPods --cli-unfold-argument  \
    --Id train-12442
```

Output: 
```
{
    "Response": {
        "PodNames": [
            "train-fdsff"
        ],
        "TotalCount": 1,
        "PodInfoList": [
            {
                "Name": "pod-abc",
                "IP": "12.23.23.14",
                "Status": "RUNNING",
                "StartTime": "2025-01-02 00:00:00",
                "EndTime": "2025-01-02 00:01:00",
                "ResourceConfigInfo": {
                    "Role": "master",
                    "Cpu": 1,
                    "Memory": 1,
                    "GpuType": "HCC",
                    "Gpu": 1,
                    "InstanceType": "fdsaf",
                    "InstanceNum": 1,
                    "InstanceTypeAlias": "fsadfd",
                    "RDMAConfig": {
                        "Enable": true
                    }
                }
            }
        ],
        "RequestId": "fdsjlk-dsfdsf"
    }
}
```

