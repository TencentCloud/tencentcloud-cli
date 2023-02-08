**Example 1: 查询数据库升级价格**



Input: 

```
tccli cdb InquiryPriceUpgradeInstances --cli-unfold-argument  \
    --InstanceId cdb-6si6qy6p \
    --Volume 50 \
    --Memory 1000
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

