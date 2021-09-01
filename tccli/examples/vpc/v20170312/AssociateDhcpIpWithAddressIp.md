**Example 1: DhcpIp绑定EIP**



Input: 

```
tccli vpc AssociateDhcpIpWithAddressIp --cli-unfold-argument  \
    --DhcpIpId dpcpip-9o233uri \
    --AddressIp 119.29.93.218
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

