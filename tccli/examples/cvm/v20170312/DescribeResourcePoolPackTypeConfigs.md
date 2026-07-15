**Example 1: 查询支持实例资源池的机型规格列表**

查询支持实例资源池的机型规格列表

Input: 

```
tccli cvm DescribeResourcePoolPackTypeConfigs --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-7
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "CPU": 256,
                "FPGA": 0,
                "GPU": 0,
                "GpuCount": 0,
                "InstanceFamily": "SA5",
                "InstanceType": "SA5.64XLARGE1152",
                "Memory": 1152,
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "0b93f550-b77f-4cf1-896e-574458fd5cb1"
    }
}
```

