**Example 1: 购买预留实例计费**

购买预留实例计费

Input: 

```
tccli cvm PurchaseReservedInstancesOffering --cli-unfold-argument  \
    --InstanceCount 2 \
    --ReservedInstancesOfferingId noew0342-324f-f3ab-9uut-wrlnth53dcee
```

Output: 
```
{
    "Response": {
        "ReservedInstanceId": "13d8e599-b8dc-4e8a-80b4-7dce9eb27043",
        "RequestId": "b333ddb8-4aed-4def-a0d9-617043c2614e"
    }
}
```

