**Example 1: 列出已购买预留实例计费**

列出已购买预留实例计费

Input: 

```
tccli cvm DescribeReservedInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name zone \
    --Filters.0.Values ap-singapore-1
```

Output: 
```
{
    "Response": {
        "RequestId": "dcb99aa2-f50d-43c6-aadd-74775f016db2",
        "ReservedInstancesSet": [
            {
                "CurrencyCode": "USD",
                "Duration": 31536000,
                "EndTime": "2024-07-30 10:59:59",
                "InstanceCount": 1,
                "InstanceFamily": "S5",
                "InstanceType": "S5.MEDIUM2",
                "OfferingType": "No Upfront",
                "ProductDescription": "linux",
                "ReservedInstanceId": "ri-je53w05q",
                "ReservedInstanceName": "Unnamed",
                "StartTime": "2023-07-31 10:00:00",
                "State": "retired",
                "Zone": "ap-singapore-1"
            }
        ],
        "TotalCount": 3
    }
}
```

