**Example 1: 调整EIP续费标识**



Input: 

```
tccli vpc ModifyAddressesRenewFlag --cli-unfold-argument  \
    --AddressIds eip-cpfph9t4 \
    --RenewFlag NOTIFY_AND_MANUAL_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "c89a8c84-6943-45ad-9342-36f599d77754"
    }
}
```

