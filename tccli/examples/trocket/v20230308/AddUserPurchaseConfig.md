**Example 1: 添加成功**

添加成功响应

Input: 

```
tccli trocket AddUserPurchaseConfig --cli-unfold-argument  \
    --CustomerAppId 1293673453 \
    --CustomerUin 112936734523 \
    --ProductSpec rocket-vip-basic-0 \
    --CustomerRegion 19 \
    --Zones 190001 \
    --MaxNodes 2 \
    --MinNodes 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "74cf1776-786c-42a4-aeab-77043c69a017"
    }
}
```

