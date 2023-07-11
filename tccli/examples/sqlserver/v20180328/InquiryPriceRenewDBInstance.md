**Example 1: 查询单个实例续费价格**

查询单个实例续费价格

Input: 

```
tccli sqlserver InquiryPriceRenewDBInstance --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl
```

Output: 
```
{
    "Response": {
        "RequestId": "41e0018d-857d-4c8c-9763-57afa2c062f9",
        "OriginalPrice": 42720,
        "Price": 42720
    }
}
```

