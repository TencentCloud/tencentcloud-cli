**Example 1: 支付订单示例**



Input: 

```
tccli billing PayDeals --cli-unfold-argument  \
    --OrderIds 2020111161300016142141 \
    --AutoVoucher 1
```

Output: 
```
{
    "Response": {
        "OrderIds": [
            "2020111161300016142141"
        ],
        "BigDealIds": [
            "2020111161300016142108"
        ],
        "ResourceIds": {
            "2020111161300016142141": [
                "ins-abc",
                "ins-xxx"
            ]
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

