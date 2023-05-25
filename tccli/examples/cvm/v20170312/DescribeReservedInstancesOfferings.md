**Example 1: 列出可购买预留实例计费**

列出可购买预留实例计费

Input: 

```
tccli cvm DescribeReservedInstancesOfferings --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReservedInstancesOfferingsSet": [
            {
                "Zone": "ap-guangzhou-1",
                "CurrencyCode": "USD",
                "Duration": 31536000,
                "FixedPrice": 4000.0,
                "InstanceType": "S3.MEDIUM4",
                "OfferingType": "All Upfront",
                "ReservedInstancesOfferingId": "noew0342-324f-f3ab-9uut-wrlnth53dcee",
                "ProductDescription": "linux",
                "UsagePrice": 0.0
            }
        ],
        "RequestId": "b813c959-cc89-41d5-9cc4-ceb7d853dcaa"
    }
}
```

