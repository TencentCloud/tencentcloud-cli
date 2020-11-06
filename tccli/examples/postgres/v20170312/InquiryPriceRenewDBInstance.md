**Example 1: Querying the renewal price of instance postgres-6fego161**



Input: 

```
tccli postgres InquiryPriceRenewDBInstance --cli-unfold-argument  \
    --DBInstanceId postgres-6fego161 \
    --Period 12
```

Output: 
```
{
    "Response": {
        "Price": 210355,
        "RequestId": "08fdf411-5d39-44f2-8e1d-a58ee60b237d",
        "OriginalPrice": 253440
    }
}
```

