**Example 1: 续费 TWeSee 视频理解订阅**



Input: 

```
tccli iotexplorer RenewTWeSeeSubscription --cli-unfold-argument  \
    --ProductId DLLNMAZ4EO \
    --DeviceName cs_test02 \
    --ServiceType VID_COMP \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "4000",
        "OrderId": "20260923311023764115441",
        "OriginalPrice": "4000",
        "ResourceId": "twesee-753yd29z71908rv8xo5g1dv",
        "Status": "DELIVERED",
        "RequestId": "e075af94-1ccf-4171-bb14-31ce419c943a"
    }
}
```

