**Example 1: 获取资源监控列表**



Input: 

```
tccli cwp DescribeAssetMachineList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "xx",
        "Machines": [
            {
                "OsInfo": "xx",
                "Uuid": "xx",
                "MemLoad": 0.0,
                "MachineName": "xx",
                "MachineIp": "xx",
                "DiskLoad": 0.0,
                "DiskSize": 1,
                "Quuid": "xx",
                "MemSize": 1,
                "PartitionCount": 1,
                "Cpu": "xx"
            }
        ]
    }
}
```

