**Example 1: 查询指定实例支持调整的机型配置**



Input: 

```
tccli cvm DescribeInstancesModification --cli-unfold-argument  \
    --InstanceIds xx \
    --Filters.0.Name status \
    --Filters.0.Values SELL
```

Output: 
```
{
    "Response": {
        "InstanceTypeConfigStatusSet": [
            {
                "Status": "SELL",
                "InstanceTypeConfig": {
                    "Zone": "ap-guangzhou-2",
                    "FPGA": 0,
                    "InstanceFamily": "SA2",
                    "InstanceType": "SA2.MEDIUM4",
                    "Memory": 4,
                    "GPU": 0,
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

