**Example 1: 退还模型路由资源包询价**

退还模型路由资源包询价

Input: 

```
tccli clb InquirePriceRefundModelRouterResourcePackage --cli-unfold-argument  \
    --ModelRouterResourcePackageIds cmrcredit-k2800toa9v5tnar
```

Output: 
```
{
    "Response": {
        "ModelRouterResourcePackageRefundPrice": [
            {
                "ModelRouterPackageId": "cmrcredit-k2800toa9v5tnar",
                "Price": 1
            }
        ],
        "RequestId": "872ed7cd-7456-4b5f-822b-69c1d78282c9"
    }
}
```

