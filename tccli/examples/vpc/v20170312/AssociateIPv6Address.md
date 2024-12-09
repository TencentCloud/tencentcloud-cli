**Example 1: 弹性公网IPv6绑定弹性网卡**

弹性公网IPv6绑定弹性网卡。

Input: 

```
tccli vpc AssociateIPv6Address --cli-unfold-argument  \
    --IPv6AddressId eipv6-3lxpc6sh \
    --NetworkInterfaceId eni-0c454zph \
    --PrivateIPv6Address fc00:200:300:700:0:9c64:2c95:b711
```

Output: 
```
{
    "Response": {
        "RequestId": "631011dd-6dfa-41b5-be7c-47bd61d82978"
    }
}
```

