**Example 1: 查询数据库实例新购价格**



Input: 

```
tccli cdb DescribeDBPrice --cli-unfold-argument  \
    --Zone ap-guangzhou-1 \
    --GoodsNum 1 \
    --Memory 1000 \
    --Volume 25 \
    --PayType PRE_PAID \
    --Period 24
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Price": 48000,
        "OriginalPrice": 460800
    }
}
```

**Example 2: 查询数据库实例续费价格**



Input: 

```
tccli cdb DescribeDBPrice --cli-unfold-argument  \
    --InstanceId cdb-6no119yd \
    --Period 24
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "Price": 48000,
        "OriginalPrice": 460800
    }
}
```

