**Example 1: 查询示例**

查询续费价格

Input: 

```
tccli redis InquiryPriceRenewInstance --cli-unfold-argument  \
    --Period 1 \
    --InstanceId crs-f21jya09
```

Output: 
```
{
    "Response": {
        "AmountUnit": "pent",
        "Currency": "CNY",
        "HighPrecisionOriginalPrice": 30400,
        "HighPrecisionPrice": 30400,
        "OriginalPrice": 30400,
        "Price": 30400,
        "RequestId": "dafd42cd-220d-44d7-b2cd-b50da5dc0002"
    }
}
```

