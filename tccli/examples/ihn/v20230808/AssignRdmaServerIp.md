**Example 1: 单卡机器首次调接口申请RDMA IP**

单卡机器首次调接口申请IP，此时返回请求ID，后续根据请求ID查异步任务信息获取RDMA IP。

Input: 

```
tccli ihn AssignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --UniqClusterId hpc-075c288a \
    --ClusterInfo.ClusterType 1 \
    --IntMask 30 \
    --ClusterInfoV2 False \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "dd214b4d-fe3d-498b-9851-d1dad89832c4"
    }
}
```

**Example 2: 单卡机器非首次调接口申请RDMA IP**

单卡机器非首次调接口申请RDMA IP，此时直接返回RDMA IP信息。

Input: 

```
tccli ihn AssignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36b2 \
    --UniqClusterId hpc-075c288a \
    --IpAddressCount 1 \
    --ClusterInfo.ClusterType 1 \
    --IntMask 30 \
    --ClusterInfoV2 False \
    --DeadlineTimeStamp 2025-02-22 17:50:48
```

Output: 
```
{
    "Response": {
        "ClusterId": 8888,
        "GatewayIp": "192.81.1.157",
        "InstanceUuid": "075c288a-cd57-4906-b1fb-f2fd6f9f36b2",
        "Mask": "255.255.255.252",
        "ModuleId": 818181,
        "ServerIp": "192.81.1.158",
        "Subnet": "192.81.1.156",
        "RequestId": "a6a0cbfb-2b47-46a2-98af-5b4913668d4a"
    }
}
```

**Example 3: 多卡机器首次调接口申请RDMA IP**

多卡机器首次调接口申请IP，此时返回请求ID，后续根据请求ID查异步任务信息获取RDMA IP。

Input: 

```
tccli ihn AssignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --UniqClusterId hpc-075c288a \
    --IpAddressCount 4 \
    --ClusterInfo.ClusterType 1 \
    --IntMask 30 \
    --ClusterInfoV2 False \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "79a67e57-e6f9-48cd-b29c-fa6fb1db1edb"
    }
}
```

**Example 4: 多卡机器非首次调接口申请RDMA IP**

多卡机器非首次调接口申请IP，此时通过IpAddresses字段直接返回RDMA IP列表。

Input: 

```
tccli ihn AssignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --UniqClusterId hpc-075c288a \
    --IpAddressCount 4 \
    --ClusterInfo.ClusterType 1 \
    --IntMask 30 \
    --ClusterInfoV2 False \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "ClusterId": 8888,
        "InstanceUuid": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
        "IpAddresses": [
            {
                "GatewayIp": "192.81.10.17",
                "Mask": "255.255.255.252",
                "ServerIp": "192.81.10.18",
                "Subnet": "192.81.10.16"
            }
        ],
        "ModuleId": 818181,
        "RequestId": "55c6cfec-47aa-4403-a3c7-70488c9207bb"
    }
}
```

**Example 5: IB机器申请PKeyId**

IB机器申请PKeyId，直接返回PKeyId的值。

Input: 

```
tccli ihn AssignRdmaServerIp --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid a2d8f6c1-5b94-4e72-9f3a-8d6e4b2c7a91 \
    --ClusterInfo.ClusterType 2
```

Output: 
```
{
    "Response": {
        "ClusterId": 9999,
        "ClusterType": 2,
        "InstanceUuid": "a2d8f6c1-5b94-4e72-9f3a-8d6e4b2c7a91",
        "ModuleId": 919191,
        "PKeyId": 1,
        "RequestId": "6421ce6f-988a-49e9-8661-16260feff57e"
    }
}
```

