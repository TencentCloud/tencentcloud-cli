**Example 1: 查询申请SqlServer实例价格**

查询申请SqlServer实例价格

Input: 

```
tccli sqlserver InquiryPriceCreateDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --Memory 2 \
    --Storage 300 \
    --Period 1 \
    --GoodsNum 1 \
    --DBVersion 2008R2
```

Output: 
```
{
    "Response": {
        "RequestId": "6ace8140-6b9e-4e81-a8ad-ef3f92b2aa90",
        "OriginalPrice": 20988,
        "Price": 20988
    }
}
```

