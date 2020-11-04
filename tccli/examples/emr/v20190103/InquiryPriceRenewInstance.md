**Example 1: 续费询价示例**



Input: 

```
tccli emr InquiryPriceRenewInstance --cli-unfold-argument  \
    --TimeUnit m\
    --TimeSpan 1\
    --Currency CNY\
    --PayMode 1\
    --ResourceIds emr-vm-jv1s4zas\
    --Placement.ProjectId 0\
    --Placement.Zone ap-guangzhou-4
```

Output: 
```
{
    "Response": {
        "DiscountCost": 596.54,
        "OriginalCost": 898.9,
        "RequestId": "223c838e-ce27-4adf-9a41-89661fe7ad21",
        "TimeSpan": 1,
        "TimeUnit": "m"
    }
}
```

