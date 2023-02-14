**Example 1: HAVIP绑定EIP**

HAVIP绑定EIP

Input: 

```
tccli vpc HaVipAssociateAddressIp --cli-unfold-argument  \
    --AddressIp 119.29.93.218 \
    --HaVipId havip-9o233uri
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb47621-838b-428e-8c33-6e210d93c451"
    }
}
```

