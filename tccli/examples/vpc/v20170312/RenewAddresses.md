**Example 1: 续费包月带宽弹性公网IP**



Input: 

```
tccli vpc RenewAddresses --cli-unfold-argument  \
    --AddressIds eip-fo00aojo\
    --AddressChargePrepaid.Period 1\
    --AddressChargePrepaid.TimeUnit m\
    --AddressChargePrepaid.AutoRenewFlag 0
```

Output: 
```
{
    "Response": {
        "DealName": "20200424114970",
        "RequestId": "076ca3ee-0fed-4576-b5b8-44fa1f3d4424"
    }
}
```

