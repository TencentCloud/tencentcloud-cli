**Example 1: 获取边缘节点信息**



Input: 

```
tccli iecp DescribeEdgeNode --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --NodeId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "7b6f5a4f-35d3-4cb4-8282-34d7062b30a3",
        "Id": 100154,
        "Kind": "Agent",
        "Name": "test01",
        "Status": 4,
        "CpuArchitecture": "",
        "AiChipArchitecture": "",
        "Ip": "",
        "Labels": [
            {
                "Key": "beta.kubernetes.io/arch",
                "Value": "amd64",
                "Protected": true
            },
            {
                "Key": "beta.kubernetes.io/os",
                "Value": "linux",
                "Protected": true
            }
        ],
        "Resource": {
            "AllocatedCPU": "3800m",
            "TotalCPU": "4",
            "AllocatedMemory": "6887172Ki",
            "TotalMemory": "8013572Ki",
            "AllocatedGPU": null,
            "TotalGPU": null,
            "AvailableCPU": null,
            "AvailableMemory": null,
            "AvailableGPU": null
        }
    }
}
```

