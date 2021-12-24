**Example 1: 查询边缘节点列表**



Input: 

```
tccli iecp DescribeEdgeNodes --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --Sort.0.Field Name \
    --Sort.0.Order ASC
```

Output: 
```
{
    "Response": {
        "RequestId": "4c815bfa-0a61-4676-91c7-452ad56a373a",
        "TotalCount": 1,
        "NodeSet": [
            {
                "Id": 100152,
                "Name": "test-test01",
                "Status": 1,
                "CpuArchitecture": "amd64",
                "Resource": {
                    "AllocatedCPU": "120m",
                    "TotalCPU": "4000m",
                    "AllocatedMemory": "0.15",
                    "TotalMemory": "7.64",
                    "AllocatedGPU": "",
                    "TotalGPU": "",
                    "AvailableCPU": "",
                    "AvailableMemory": "6.42",
                    "AvailableGPU": "0"
                },
                "Ip": "192.168.8.102",
                "CreateTime": "2021-01-01 11:00:00",
                "OperatingSystem": "CentOS Linux 7 (Core)",
                "NodeUnits": null
            }
        ]
    }
}
```

