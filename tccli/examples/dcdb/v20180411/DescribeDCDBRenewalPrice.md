**Example 1: 查询分布式数据库实例续费的价格**



Input: 

```
tccli dcdb DescribeDCDBRenewalPrice --cli-unfold-argument  \
    --InstanceId dcdvt-fdpjf5zh \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5b637383-8059-b0f8-3dcd-59fbdff262b6",
        "OriginalPrice": 42240,
        "Price": 42240
    }
}
```

