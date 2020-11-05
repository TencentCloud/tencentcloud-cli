**Example 1: Adjusting the pay-as-you-go bandwidth**



Input: 

```
tccli vpc ModifyAddressesBandwidth --cli-unfold-argument  \
    --InternetMaxBandwidthOut 2\
    --AddressIds eip-alfxy9c8
```

Output: 
```
{
    "Response": {
        "TaskId": "11531422",
        "RequestId": "24cfceab-3492-482c-b86f-27f598b1b044"
    }
}
```

