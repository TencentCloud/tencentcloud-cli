**Example 1: 示例**



Input: 

```
tccli clouddc ImportOfflineProduct --cli-unfold-argument  \
    --OrganizationUin 12334556 \
    --GoodsList.0.customer_uin 123 \
    --GoodsList.0.customer_name 123 \
    --GoodsList.0.goods_name 123 \
    --GoodsList.0.amount 123 \
    --GoodsList.0.comment 123 \
    --AccessToken 1
```

Output: 
```
{
    "Response": {
        "JsonString": "{}",
        "RequestId": "c709efd4-be95-486f-aabe-773651795402"
    }
}
```

