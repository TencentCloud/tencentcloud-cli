**Example 1: 测试示例**



Input: 

```
tccli opc SyncProductIntroPageData --cli-unfold-argument  \
    --DataList.0.CloudProductName 云服务器 \
    --DataList.0.ResourceUrl https://cloud.tencent.com/act/pro/samtest20200509 \
    --DataList.0.Title 测试 \
    --DataList.0.CloudProductCode cvm \
    --DataList.0.OwnerList jensens \
    --DataList.0.Module banner \
    --DataList.0.ReleaseStatus 1 \
    --DataList.0.Operator jensens \
    --DataList.0.ProductIntroPageUrl https://cloud.tencent.com/product/cvm \
    --DataList.0.ReleaseTime 2022-08-15 00:00:00
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Result": "ok",
                "Url": "https://cloud.tencent.com/act/pro/samtest20200509"
            }
        ],
        "RequestId": "f9125e55-6749-4a90-9954-15f2929d53ea"
    }
}
```

