**Example 1: 批量调整弹性公网IPv6地址名称**

批量调整弹性公网IPv6地址名称。

Input: 

```
tccli vpc ModifyIPv6AddressesAttributes --cli-unfold-argument  \
    --IPv6AddressIds eipv6-2ucdpy9t eipv6-3lxpc6sh \
    --IPv6AddressName test
```

Output: 
```
{
    "Response": {
        "RequestId": "a75d9b1a-0640-43a2-837b-6334247e9fbc"
    }
}
```

