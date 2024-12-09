**Example 1: 解绑弹性公网IPv6**

解绑弹性公网IPv6。

Input: 

```
tccli vpc DisassociateIPv6Address --cli-unfold-argument  \
    --IPv6AddressId eipv6-or8cse19
```

Output: 
```
{
    "Response": {
        "RequestId": "631011dd-6dfa-41b5-be7c-47bd61d82978"
    }
}
```

