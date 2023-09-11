**Example 1: 查询各个 规格Pod 的抵扣率**

可被预留券抵扣的 Pod 的抵扣率查询

Input: 

```
tccli tke DescribePodDeductionRate --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0be873cf-014f-408b-8527-03c25c32725b",
        "PodDeductionRateSet": [
            {
                "DeductionNum": 0,
                "TotalNum": 1,
                "Cpu": 0.5,
                "Memory": 1,
                "Type": "intel",
                "GpuNum": ""
            },
            {
                "DeductionNum": 0,
                "TotalNum": 2,
                "Cpu": 1,
                "Memory": 1,
                "Type": "intel",
                "GpuNum": ""
            },
            {
                "DeductionNum": 0,
                "TotalNum": 5,
                "Cpu": 1,
                "Memory": 2,
                "Type": "intel",
                "GpuNum": ""
            },
            {
                "DeductionNum": 0,
                "TotalNum": 4,
                "Cpu": 1,
                "Memory": 2,
                "Type": "amd",
                "GpuNum": ""
            },
            {
                "DeductionNum": 0,
                "TotalNum": 1,
                "Cpu": 2,
                "Memory": 4,
                "Type": "amd",
                "GpuNum": ""
            },
            {
                "DeductionNum": 1,
                "TotalNum": 1,
                "Cpu": 8,
                "Memory": 16,
                "Type": "intel",
                "GpuNum": ""
            }
        ]
    }
}
```

