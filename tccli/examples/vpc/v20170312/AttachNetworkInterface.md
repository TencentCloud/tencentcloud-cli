**Example 1: 弹性网卡绑定云服务器**

弹性网卡绑定云服务器

Input: 

```
tccli vpc AttachNetworkInterface --cli-unfold-argument  \
    --NetworkInterfaceId eni-afo43z61 \
    --InstanceId ins-ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c"
    }
}
```

