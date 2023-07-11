**Example 1: 续费询价示例**

续费询价示例

Input: 

```
tccli emr InquiryPriceRenewInstance --cli-unfold-argument  \
    --Placement.ProjectId 0 \
    --Placement.Zone ap-guangzhou-4 \
    --Currency CNY \
    --TimeSpan 1 \
    --PayMode 1 \
    --ResourceIds emr-vm-jv1s4zas \
    --TimeUnit m
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

**Example 2: 续费询价**

续费询价

Input: 

```
tccli emr InquiryPriceRenewInstance --cli-unfold-argument  \
    --TimeUnit abc \
    --TimeSpan 1 \
    --ResourceIds abc \
    --Currency abc \
    --Placement.ProjectId 0 \
    --Placement.Zone abc \
    --PayMode 0 \
    --ModifyPayMode 0
```

Output: 
```
{
    "Response": {
        "OriginalCost": 0,
        "DiscountCost": 0,
        "TimeUnit": "abc",
        "TimeSpan": 0,
        "RequestId": "abc"
    }
}
```

