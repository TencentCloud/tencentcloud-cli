**Example 1: 购买预留实例计费**

购买预留实例计费

Input: 

```
tccli cvm PurchaseReservedInstancesOffering --cli-unfold-argument  \
    --InstanceCount 2 \
    --ReservedInstancesOfferingId 694e115d-e1b2-47f5-8217-bfbdea222da1 \
    --ReservedInstanceName MyReservedInstanceName
```

Output: 
```
{
    "Response": {
        "ReservedInstanceId": "ri-8frq127i",
        "RequestId": "b333ddb8-4aed-4def-a0d9-617043c2614e"
    }
}
```

