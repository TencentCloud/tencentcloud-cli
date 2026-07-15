**Example 1: 单卡机器退还RDMA IP**

单卡机器退还RDMA IP

Input: 

```
tccli ihn UnassignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --UniqClusterId hpc-075c288a \
    --ClusterInfo.ClusterType 1 \
    --ServerIp 192.81.1.190 \
    --Subnet 192.81.1.188 \
    --Mask 255.255.255.252 \
    --GatewayIp 192.81.1.189 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "e7326e28-298f-4dcb-a2ea-8064eb1dddd5"
    }
}
```

**Example 2: 多卡机器退还RDMA IP**

多卡机器退还RDMA IP

Input: 

```
tccli ihn UnassignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --RdmaIpAddresses.0.ServerIp 192.81.1.174
```

Output: 
```
{
    "Response": {
        "RequestId": "25ed9088-74e7-4ce0-8b97-b67774fee2dc"
    }
}
```

**Example 3: IB机器退还PkeyId**

IB机器退还PkeyId，注意无需传PkeyId

Input: 

```
tccli ihn UnassignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid 3e9a1f5d-7c42-4b89-a6d3-9f8b2e4c1a7d \
    --ClusterInfo.ClusterType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "351a6a34-994b-46a0-932a-a4c67c654729"
    }
}
```

