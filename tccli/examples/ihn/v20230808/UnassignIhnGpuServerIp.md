**Example 1: 单卡机器退还RDMA IP**

单卡机器退还RDMA IP

Input: 

```
tccli ihn UnassignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d \
    --UniqClusterId hpc-6f9f36b2 \
    --ClusterInfo.ClusterType 1 \
    --ClusterInfo.CdcId cluster-b5c7e2a9 \
    --ClusterInfo.ChcId chc-4d3c9a2b \
    --ClusterInfo.IsPhysicalClusterPreCreated False \
    --ServerIp 192.81.10.18 \
    --Subnet 192.81.10.16 \
    --Mask 255.255.255.252 \
    --GatewayIp 192.81.10.17 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "dbd42b9f-9cff-470a-9b3a-97e0f473c6fa"
    }
}
```

**Example 2: 多卡机器退还RDMA IP**

多卡机器退还RDMA IP

Input: 

```
tccli ihn UnassignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8321 \
    --InstanceUuid b5c7e2a9-4f81-4d3c-9a2b-6e8f3d1c5a94 \
    --ClusterInfo.ClusterType 1 \
    --ClusterInfo.CdcId cluster-b5c7e2a9 \
    --ClusterInfo.ChcId chc-4d3c9a2b \
    --ClusterInfo.IsPhysicalClusterPreCreated False \
    --DeadlineTimeStamp 2025-02-22 17:50:46 \
    --RdmaIpAddresses.0.ServerIp 192.81.10.134
```

Output: 
```
{
    "Response": {
        "RequestId": "f6ba582e-db6a-4bfd-8964-7cf151e614ce"
    }
}
```

**Example 3: IB机器退还PkeyId**

IB机器退还PkeyId，注意无需传PkeyId

Input: 

```
tccli ihn UnassignIhnGpuServerIp --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid 351a6a34-994b-46a0-932a-a4c67c655830 \
    --ClusterInfo.ClusterType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "aece7980-6d1e-42c9-8ef6-c7e2cc180bc8"
    }
}
```

