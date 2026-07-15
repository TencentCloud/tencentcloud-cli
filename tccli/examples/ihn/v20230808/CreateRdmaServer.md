**Example 1: IB机器创建服务器**

IB机器创建服务器

Input: 

```
tccli ihn CreateRdmaServer --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid cb9da3ec-e96e-4fab-ad85-e96e4fabad85 \
    --ClusterInfo.ClusterType 2 \
    --HostIp 8.1.111.9 \
    --GUID 491a7f3c47145acf \
    --PKeyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "45052d15-6d19-4f54-8cbb-23951714b273"
    }
}
```

**Example 2: 单卡机器创建GPU服务器**

单卡机器创建GPU服务器

Input: 

```
tccli ihn CreateRdmaServer --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36b2 \
    --UniqClusterId hpc-5b944e72 \
    --ClusterInfo.ClusterType 1 \
    --HostIp 8.8.111.1 \
    --ServerIp 192.81.1.158 \
    --DeadlineTimeStamp 2025-02-22 17:50:46 \
    --Subnet 192.81.1.156 \
    --Mask 255.255.255.252 \
    --GatewayIp 192.81.1.157
```

Output: 
```
{
    "Response": {
        "RequestId": "fa8d6a33-2576-447f-b993-d8bb7df9c4db"
    }
}
```

**Example 3: 多卡机器创建GPU服务器**

多卡机器创建GPU服务器

Input: 

```
tccli ihn CreateRdmaServer --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --ClusterInfo.ClusterType 1 \
    --HostIp 8.1.111.111 \
    --DeadlineTimeStamp 2025-02-22 17:50:46 \
    --RdmaIpAddresses.0.ServerIp 192.81.1.174
```

Output: 
```
{
    "Response": {
        "RequestId": "7c1560ec-5b2e-439c-aa18-c3a26391a555"
    }
}
```

