**Example 1: 包年包月转按量计费**



Input: 

```
tccli redis ModifyInstanceChargeType --cli-unfold-argument  \
    --InstanceIds crs-fdfavarz \
    --InstanceChargeType POSTPAID
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "7ec26376-733c-4889-92e5-acb3a14fa8ec"
    }
}
```

**Example 2: 按量计费转包年包月**



Input: 

```
tccli redis ModifyInstanceChargeType --cli-unfold-argument  \
    --InstanceIds crs-4xdghyew \
    --InstanceChargeType PREPAID \
    --Period 1
```

Output: 
```
{
    "Response": {
        "FailedInstanceIds": [],
        "RequestId": "bf20dfeb-894e-410f-8973-93cb29e0b9cf"
    }
}
```

