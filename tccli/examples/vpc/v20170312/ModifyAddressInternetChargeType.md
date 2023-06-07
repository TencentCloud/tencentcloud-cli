**Example 1: 调整弹性公网IP计费模式**

调整弹性公网IP计费模式。

Input: 

```
tccli vpc ModifyAddressInternetChargeType --cli-unfold-argument  \
    --AddressId eip-fo00aojo \
    --InternetChargeType TRAFFIC_POSTPAID_BY_HOUR \
    --InternetMaxBandwidthOut 5
```

Output: 
```
{
    "Response": {
        "RequestId": "a3524d83-9f3b-40ee-beb8-3a8144e7d125"
    }
}
```

