**Example 1: 查询实例机型列表**

查询广州二区中实例机型系列为I1的机型列表

Input: 

```
tccli cvm DescribeInstanceTypeConfigs --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-2 \
    --Filters.1.Name instance-family \
    --Filters.1.Values I1
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM4",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 4,
                "GpuCount": 0
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM8",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 8,
                "GpuCount": 0
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM16",
                "CPU": 2,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 16,
                "GpuCount": 0
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.LARGE8",
                "CPU": 4,
                "GPU": 0,
                "FPGA": 0,
                "Memory": 8,
                "GpuCount": 0
            }
        ],
        "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
    }
}
```

