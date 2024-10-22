**Example 1: 获取资源监控列表**

获取资源监控列表

Input: 

```
tccli cwp DescribeAssetMachineList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Machines": [
            {
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "MachineIp": "10.0.0.11",
                "MachineName": "test-name",
                "OsInfo": "CentOs Bit64",
                "Cpu": "Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz",
                "MemSize": 1,
                "MemLoad": "abc",
                "DiskSize": 1,
                "DiskLoad": "abc",
                "PartitionCount": 1,
                "MachineWanIp": "110.84.0.11",
                "ProjectId": 1,
                "CpuSize": 1,
                "CpuLoad": "Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz",
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "UpdateTime": "2024-10-11 12:23:34",
                "IsNew": 0,
                "FirstTime": "2024-10-11 12:23:34",
                "MachineExtraInfo": {
                    "WanIP": "110.84.0.11",
                    "PrivateIP": "10.0.0.11",
                    "NetworkType": 0,
                    "NetworkName": "vpc-12341234",
                    "InstanceID": "ins-aj28fjz",
                    "HostName": "test-name"
                }
            }
        ],
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

