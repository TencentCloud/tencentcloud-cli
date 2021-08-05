**Example 1: 商户查询正常示例**

商户查询正常的示例

Input: 

```
tccli cpdp QueryMerchant --cli-unfold-argument  \
    --MerchantAppId 34edsdfa
```

Output: 
```
{
    "Response": {
        "RequestId": "fd590936-acd7-440c-9ac5-b698bc0a5af0",
        "MerchantAppId": "1c6f41570498301d85fc4589a5435b54",
        "MerchantName": "测试商户",
        "BusinessPayFlag": "1"
    }
}
```

