**Example 1: 查询实例扩容价格**

查询实例扩容价格

Input: 

```
tccli sqlserver InquiryPriceUpgradeDBInstance --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Memory 8 \
    --Storage 300
```

Output: 
```
{
    "Response": {
        "RequestId": "dcff5304-324e-4cd6-a5f2-02cb16bde2da",
        "OriginalPrice": 149696,
        "Price": 149696
    }
}
```

