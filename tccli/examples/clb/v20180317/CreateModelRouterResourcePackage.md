**Example 1: 创建模型路由资源包**

创建模型路由资源包

Input: 

```
tccli clb CreateModelRouterResourcePackage --cli-unfold-argument  \
    --ModelRouterResourcePackageAmount 100 \
    --AutoPurchaseFlag 0
```

Output: 
```
{
    "Response": {
        "DealName": "20260409643022548203771",
        "ModelRouterResourcePackageIds": [
            "cmrcredit-k2800toa9um7rar"
        ],
        "RequestId": "268ce293-5068-44e3-a95b-9960ca90b4bc"
    }
}
```

**Example 2: 创建模型路由资源包自动使用代金券**

创建模型路由资源包自动使用代金券

Input: 

```
tccli clb CreateModelRouterResourcePackage --cli-unfold-argument  \
    --ModelRouterResourcePackageAmount 1000 \
    --AutoPurchaseFlag 1 \
    --AutoVoucher True
```

Output: 
```
{
    "Response": {
        "DealName": "20260605096022961665431",
        "ModelRouterResourcePackageIds": [
            "cmrcredit-k4100tomk8hcni8"
        ],
        "RequestId": "b341631d-8996-4e49-941d-9e1a0040f845"
    }
}
```

