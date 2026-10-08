**Example 1: 开通 TWeSee 视频理解基础版**



Input: 

```
tccli iotexplorer CreateTWeSeeSubscription --cli-unfold-argument  \
    --ProductId default \
    --DeviceName dev0923 \
    --ServiceType VID_COMP \
    --ServiceTier BASIC \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "2000",
        "OrderId": "20260923417023758815491",
        "OriginalPrice": "2000",
        "ResourceId": "twesee-753yd29z8czyqn8lpvcxekj",
        "Status": "DELIVERED",
        "RequestId": "ead581f8-936e-4e50-8de6-76cc431b2367"
    }
}
```

**Example 2: 开通 TWeSee 视频理解高级版**



Input: 

```
tccli iotexplorer CreateTWeSeeSubscription --cli-unfold-argument  \
    --ProductId 69E4CNU1F0 \
    --DeviceName 10002 \
    --ServiceType VID_COMP \
    --ServiceTier ADVANCED \
    --Period 1
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "DiscountPrice": "4000",
        "OrderId": "20260928990179696733571",
        "OriginalPrice": "4000",
        "ResourceId": "twesee-753yd29zazzcjodjbaplog3",
        "Status": "DELIVERED",
        "RequestId": "b4a8bcd8-8c44-4e9f-ad72-4a73ebc17dfd"
    }
}
```

