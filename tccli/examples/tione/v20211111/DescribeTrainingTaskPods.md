**Example 1: pod列表**

获取任务对应的pod列表

Input: 

```
tccli tione DescribeTrainingTaskPods --cli-unfold-argument  \
    --Id abc
```

Output: 
```
{
    "Response": {
        "PodNames": [
            "abc"
        ],
        "TotalCount": 1,
        "PodInfoList": [
            {
                "Name": "abc",
                "IP": "abc",
                "Status": "abc",
                "StartTime": "abc",
                "EndTime": "abc",
                "ResourceConfigInfo": {
                    "Role": "abc",
                    "Cpu": 1,
                    "Memory": 1,
                    "GpuType": "abc",
                    "Gpu": 1,
                    "InstanceType": "abc",
                    "InstanceNum": 1,
                    "InstanceTypeAlias": "abc",
                    "RDMAConfig": {
                        "Enable": true
                    }
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

