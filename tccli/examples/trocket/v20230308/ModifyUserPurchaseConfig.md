**Example 1: 修改成功**

修改成功响应

Input: 

```
tccli trocket ModifyUserPurchaseConfig --cli-unfold-argument  \
    --CustomerAppId 123 \
    --CustomerUin 123 \
    --Config.ProductSpec rocket-vip-basic-0 \
    --Config.Region 19 \
    --Config.Zone 190001 \
    --Config.MaxNodes 10 \
    --Config.MinNodes 2 \
    --Config.SoldOut True \
    --Config.AppId 123 \
    --Config.Uin 123
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "b361c02f-283e-4791-b8d5-34ed3f79deb5"
    }
}
```

