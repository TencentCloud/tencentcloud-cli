**Example 1: 消费订单查询正常示例**

消费订单查询正常的示例

Input: 

```
tccli cpdp QueryMerchantOrder --cli-unfold-argument  \
    --OrderNo 1c6f41570498301d85fc4589a5435b54 \
    --MerchantAppId T03210722000014555992
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "MerchantAppId": "1c6f41570498301d85fc4589a5435b54",
        "OrderNo": "847f33d665d83eecaf0a8805a2ee6c7a",
        "Status": "1"
    }
}
```

