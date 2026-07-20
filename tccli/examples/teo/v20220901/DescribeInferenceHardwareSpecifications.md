**Example 1: 查询硬件规格列表**



Input: 

```
tccli teo DescribeInferenceHardwareSpecifications --cli-unfold-argument  \
    --ZoneId zone-1z***xx
```

Output: 
```
{
    "Response": {
        "HardwareSpecifications": [
            {
                "CPUNum": 16,
                "GPUMemSize": 24576,
                "GPUNum": 1,
                "MemSize": 32768,
                "Name": "基础版",
                "Spec": "spec-2n*****7"
            }
        ],
        "RequestId": "2d227629-1731-4f3f-a991-e11af1e86148"
    }
}
```

