**Example 1: 单卡机器首次调接口申请RDMA IP**

单卡机器首次调接口申请IP，此时返回请求ID，后续根据请求ID查异步任务信息获取RDMA IP。

Input: 

```
tccli ihn AssignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d \
    --UniqClusterId hpc-075c399b \
    --IpAddressCount 1 \
    --ClusterInfo.ClusterType 1 \
    --ClusterInfo.CdcId cluster-3e9a1f5d \
    --ClusterInfo.ChcId chc-2e4c1a7d \
    --ClusterInfo.IsPhysicalClusterPreCreated False \
    --DeadlineTimeStamp 2025-02-22 17:50:46 \
    --UsageScenario.Scenario CONTAINER \
    --UsageScenario.ContainerInfo.IntMaskForSupportMaxNumbers 28 \
    --UsageScenario.ContainerInfo.HostArchitecture V1
```

Output: 
```
{
    "Response": {
        "RequestId": "392ca5f5-c815-44f3-8db3-74a53d655505"
    }
}
```

**Example 2: 单卡机器非首次调接口申请RDMA IP**

单卡机器非首次调接口申请RDMA IP，此时直接返回RDMA IP信息。

Input: 

```
tccli ihn AssignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d \
    --UniqClusterId hpc-075c399b \
    --IpAddressCount 1 \
    --ClusterInfo.ClusterType 1 \
    --DeadlineTimeStamp 2025-02-22 17:50:46 \
    --UsageScenario.Scenario CONTAINER \
    --UsageScenario.ContainerInfo.IntMaskForSupportMaxNumbers 28 \
    --UsageScenario.ContainerInfo.HostArchitecture V1
```

Output: 
```
{
    "Response": {
        "ClusterId": 8888,
        "GatewayIp": "192.81.10.17",
        "InstanceUuid": "3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d",
        "Mask": "255.255.255.240",
        "ModuleId": 818181,
        "ServerIp": "192.81.10.18",
        "Subnet": "192.81.10.16",
        "RequestId": "d4e06f06-8f61-4cea-9384-12bcfa67f9ae"
    }
}
```

**Example 3: 多卡机器首次调接口申请RDMA IP**

多卡机器首次调接口申请IP，此时返回请求ID，后续根据请求ID查异步任务信息获取RDMA IP。

Input: 

```
tccli ihn AssignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8321 \
    --InstanceUuid b5c7e2a9-4f81-4d3c-9a2b-6e8f3d1c5a94 \
    --UniqClusterId hpc-3d1c5a94 \
    --IpAddressCount 2 \
    --ClusterInfo.ClusterType 1 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "418b05fb-234a-4785-b5b4-9e607aa94193"
    }
}
```

**Example 4: 多卡机器非首次调接口申请RDMA IP**

多卡机器非首次调接口申请IP，此时通过IpAddresses字段直接返回RDMA IP列表。

Input: 

```
tccli ihn AssignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8321 \
    --InstanceUuid b5c7e2a9-4f81-4d3c-9a2b-6e8f3d1c5a94 \
    --UniqClusterId hpc-3d1c5a94 \
    --IpAddressCount 2 \
    --ClusterInfo.ClusterType 1 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "ClusterId": 8321,
        "InstanceUuid": "b5c7e2a9-4f81-4d3c-9a2b-6e8f3d1c5a94",
        "IpAddresses": [
            {
                "GatewayIp": "192.81.10.133",
                "Mask": "255.255.255.252",
                "ServerIp": "192.81.10.134",
                "Subnet": "192.81.10.132"
            }
        ],
        "ModuleId": 818181,
        "RequestId": "7d4e0e16-cde0-4f25-b448-d3e07a4f550b"
    }
}
```

**Example 5: IB机器申请PKeyId**

IB机器申请PKeyId，直接返回PKeyId的值。

Input: 

```
tccli ihn AssignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid 3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d \
    --ClusterInfo.ClusterType 2 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "ClusterId": 9999,
        "ClusterType": 2,
        "InstanceUuid": "3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d",
        "ModuleId": 919191,
        "PKeyId": 1,
        "RequestId": "3f5818dc-c789-4186-85dd-7c1f48bea2ea"
    }
}
```

