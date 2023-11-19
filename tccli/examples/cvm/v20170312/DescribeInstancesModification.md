**Example 1: 查询指定实例支持调整的机型配置**

查询指定实例支持调整的机型配置

Input: 

```
tccli cvm DescribeInstancesModification --cli-unfold-argument  \
    --Filters.0.Values SELL \
    --Filters.0.Name status \
    --InstanceIds ins-bzps2kwdg
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigStatusSet": [
            {
                "Status": "SELL",
                "InstanceTypeConfig": {
                    "GPU": 0,
                    "Zone": "ap-guangzhou-2",
                    "FPGA": 0,
                    "InstanceFamily": "SA2",
                    "InstanceType": "SA2.MEDIUM4",
                    "Memory": 4,
                    "GpuCount": 0,
                    "CPU": 2
                },
                "Message": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

