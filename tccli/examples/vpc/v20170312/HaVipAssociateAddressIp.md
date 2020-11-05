**Example 1: Binding an EIP to HAVIP**



Input: 

```
tccli vpc HaVipAssociateAddressIp --cli-unfold-argument  \
    --HaVipId havip-9o233uri\
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

