**Example 1: 查询内部领用实例机型库存**

查询内部领用实例机型库存

Input: 

```
tccli cxm DescribeZoneInstanceTypeInventory --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-tianjin-2 \
    --Filters.1.Name pool \
    --Filters.1.Values qcloud_ziyan_eks \
    --Filters.2.Name instance-family \
    --Filters.2.Values S5 \
    --UseLargeScaleCpuRes True
```

Output: 
```
{
    "Response": {
        "InstanceTypeQuotaSet": [
            {
                "Zone": "ap-tianjin-2",
                "InstanceType": "S5.16XLARGE192",
                "Cpu": 64,
                "Memory": 192,
                "InstanceFamily": "S5",
                "Gpu": 0,
                "GpuCount": 0,
                "Fpga": 0,
                "Inventory": 0,
                "ReservedInventory": 0
            },
            {
                "Zone": "ap-tianjin-2",
                "InstanceType": "S5.16XLARGE256",
                "Cpu": 64,
                "Memory": 256,
                "InstanceFamily": "S5",
                "Gpu": 0,
                "GpuCount": 0,
                "Fpga": 0,
                "Inventory": 0,
                "ReservedInventory": 0
            },
            {
                "Zone": "ap-tianjin-2",
                "InstanceType": "S5.19XLARGE256",
                "Cpu": 76,
                "Memory": 256,
                "InstanceFamily": "S5",
                "Gpu": 0,
                "GpuCount": 0,
                "Fpga": 0,
                "Inventory": 0,
                "ReservedInventory": 0
            }
        ],
        "RequestId": "96ac7e0d-778b-4ed3-95a4-e9b355065292"
    }
}
```

