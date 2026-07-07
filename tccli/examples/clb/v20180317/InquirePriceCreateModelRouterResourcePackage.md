**Example 1: 创建模型路由资源包询价**

创建模型路由资源包询价

Input: 

```
tccli clb InquirePriceCreateModelRouterResourcePackage --cli-unfold-argument  \
    --ModelRouterResourcePackageAmount 100000
```

Output: 
```
{
    "Response": {
        "FirstBuy": 1,
        "ModelRouterResourcePackagePrice": {
            "ChargeUnit": null,
            "Discount": 100,
            "DiscountPrice": 1000,
            "OriginalPrice": 1000,
            "UnitPrice": null,
            "UnitPriceDiscount": null
        },
        "RequestId": "8284cd85-3ece-4584-8584-cc3143b19bdb"
    }
}
```

