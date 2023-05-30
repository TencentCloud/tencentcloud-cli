**Example 1: 续费包月带宽弹性公网IP**

续费包月带宽弹性公网IP。

Input: 

```
tccli vpc RenewAddresses --cli-unfold-argument  \
    --AddressIds eip-12345678 \
    --AddressChargePrepaid.Period 0 \
    --AddressChargePrepaid.AutoRenewFlag 0
```

Output: 
```
{
    "Response": {
        "RequestId": "076ca3ee-0fed-4576-b5b8-44fa1f3d4424"
    }
}
```

