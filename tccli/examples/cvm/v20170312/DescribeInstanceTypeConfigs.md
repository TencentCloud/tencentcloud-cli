**Example 1: 查询实例机型列表**

查询广州六区中实例机型系列为I1的机型列表

Input: 

```
tccli cvm DescribeInstanceTypeConfigs --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-6 \
    --Filters.1.Name instance-family \
    --Filters.1.Values S6
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "CPU": 4,
                "FPGA": 0,
                "GPU": 0,
                "GpuCount": 0,
                "InstanceFamily": "S6",
                "InstanceType": "S6.LARGE8",
                "Memory": 8,
                "Zone": "ap-guangzhou-6"
            },
            {
                "CPU": 2,
                "FPGA": 0,
                "GPU": 0,
                "GpuCount": 0,
                "InstanceFamily": "S6",
                "InstanceType": "S6.MEDIUM8",
                "Memory": 8,
                "Zone": "ap-guangzhou-6"
            },
            {
                "CPU": 8,
                "FPGA": 0,
                "GPU": 0,
                "GpuCount": 0,
                "InstanceFamily": "S6",
                "InstanceType": "S6.2XLARGE16",
                "Memory": 16,
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RequestId": "b809b32e-c2b9-4b71-84dd-b9ffaac904aa"
    }
}
```

