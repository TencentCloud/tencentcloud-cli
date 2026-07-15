**Example 1: 修改实例名称**

修改指定实例的名称。

Input: 

```
tccli edgezone ModifyInstanceAttribute --cli-unfold-argument  \
    --InstanceId bms-abcd1234 \
    --InstanceName new-instance-name
```

Output: 
```
{
    "Response": {
        "RequestId": "e5f6a789-4c3d-5b2e-af01-8d7c6b5a4e3f"
    }
}
```

**Example 2: 变更公网IPv4**

变更指定实例的公网IPv4地址。

Input: 

```
tccli edgezone ModifyInstanceAttribute --cli-unfold-argument  \
    --InstanceId bms-abcd1234 \
    --NewPublicIp 203.0.113.20 \
    --IpType ipv4
```

Output: 
```
{
    "Response": {
        "RequestId": "e5f6a789-4c3d-5b2e-af01-8d7c6b5a4e3f"
    }
}
```

