**Example 1: 查询价格**

查询LightHouse实例价格

Input: 

```
tccli tcb InquireVmPrice --cli-unfold-argument  \
    --Type LightHouse \
    --LightHouseBundleId bundle_rs_mc_med1_02 \
    --LightHouseBlueprintId lhbp-3qjk6slu
```

Output: 
```
{
    "Response": {
        "Currency": "CNY",
        "Discount": 100,
        "DiscountCredits": 1333.3334,
        "DiscountPrice": 40,
        "OriginalCredits": 1333.3334,
        "OriginalPrice": 40,
        "RequestId": "6e898b9d-19e4-4a46-b26a-86f74a459ca6"
    }
}
```

