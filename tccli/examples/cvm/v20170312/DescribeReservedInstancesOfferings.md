**Example 1: 列出可购买预留实例计费**

列出可购买预留实例计费

Input: 

```
tccli cvm DescribeReservedInstancesOfferings --cli-unfold-argument  \
    --Offset 0 \
    --Limit 3 \
    --Filters.0.Name zone \
    --Filters.0.Values ap-singapore-1
```

Output: 
```
{
    "Response": {
        "RequestId": "0aca8cc9-8812-477f-b442-10cc1a701d48",
        "ReservedInstancesOfferingsSet": [
            {
                "CurrencyCode": "USD",
                "Duration": 31536000,
                "FixedPrice": 412,
                "InstanceType": "S5.LARGE8",
                "OfferingType": "Partial Upfront",
                "ProductDescription": "linux",
                "ReservedInstancesOfferingId": "f5ededc6-5057-4863-a61b-fe96b4b96eb5",
                "UsagePrice": 0.05,
                "Zone": "ap-singapore-1"
            },
            {
                "CurrencyCode": "USD",
                "Duration": 31536000,
                "FixedPrice": 0,
                "InstanceType": "S5.LARGE8",
                "OfferingType": "No Upfront",
                "ProductDescription": "linux",
                "ReservedInstancesOfferingId": "7330ec0e-0ee2-4358-a429-4002c936c24d",
                "UsagePrice": 0.1,
                "Zone": "ap-singapore-1"
            },
            {
                "CurrencyCode": "USD",
                "Duration": 31536000,
                "FixedPrice": 1200,
                "InstanceType": "S5.LARGE16",
                "OfferingType": "All Upfront",
                "ProductDescription": "linux",
                "ReservedInstancesOfferingId": "e26bfbf3-85fa-4c88-82a8-0dd2706e60db",
                "UsagePrice": 0,
                "Zone": "ap-singapore-1"
            }
        ],
        "TotalCount": 20
    }
}
```

