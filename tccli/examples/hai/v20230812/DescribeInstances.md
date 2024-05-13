**Example 1: 查看指定实例hai-jklfaded的信息**

查看指定实例hai-jklfaded的信息

Input: 

```
tccli hai DescribeInstances --cli-unfold-argument  \
    --InstanceIds hai-jklfaded \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 10,
        "InstanceSet": [
            {
                "InstanceId": "hai-jklfaded",
                "InstanceName": "abc",
                "InstanceState": "RUNNING",
                "ApplicationName": "pytorch",
                "BundleName": "基础型",
                "GPUPerformance": "8+TFlops",
                "GPUMemory": "16+GB",
                "CPU": "20C",
                "Memory": "80GB",
                "SystemDisk": {
                    "DiskType": "CLOUD_SSD",
                    "DiskSize": 80
                },
                "PrivateIpAddresses": [
                    "1.1.1.1"
                ],
                "PublicIpAddresses": [
                    "2.2.2.2"
                ],
                "SecurityGroupIds": [
                    "sg-xxxxxxxx"
                ],
                "LatestOperation": "RunInstances",
                "LatestOperationState": "SUCCESS",
                "CreateTime": "2023-08-01 00:00:00",
                "MaxOutBandwidth": "10Mbps",
                "MaxFreeTraffic": "1000GB",
                "ConfigurationEnvironment": "cuda 10 | pytorch | tensorflow",
                "LoginServices": [
                    {
                        "ServiceName": "jupyter"
                    }
                ],
                "OSType": "linux"
            }
        ],
        "RequestId": "41fa870d-8592-493c-b794-9fe19f23e800"
    }
}
```

