**Example 1: 单卡机器删除GPU服务器**

单卡机器删除GPU服务器

Input: 

```
tccli ihn DeleteRdmaServer --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36b2 \
    --UniqClusterId hpc-6f9f36b2 \
    --ClusterInfo.ClusterType 1 \
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
        "RequestId": "c6f0874e-b5fd-416d-846a-7727c93107b9"
    }
}
```

**Example 2: 多卡机器删除GPU服务器**

多卡机器删除GPU服务器

Input: 

```
tccli ihn DeleteRdmaServer --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuid 075c288a-cd57-4906-b1fb-f2fd6f9f36c3 \
    --ClusterInfo.ClusterType 1 \
    --RdmaIpAddresses.0.ServerIp 192.81.1.174
```

Output: 
```
{
    "Response": {
        "RequestId": "1ef451eb-a39f-4152-a41c-7ec6d7d44a47"
    }
}
```

**Example 3: IB机器删除服务器**

IB机器删除服务器

Input: 

```
tccli ihn DeleteRdmaServer --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuid cb9da3ec-e96e-4fab-ad85-e96e4fabad85 \
    --ClusterInfo.ClusterType 2 \
    --GUID 491a7f3c47145acf \
    --PKeyId 1 \
    --DeadlineTimeStamp 2025-02-22 17:50:46
```

Output: 
```
{
    "Response": {
        "RequestId": "51748f4b-3f02-44fd-b86c-224e8414ce50"
    }
}
```

