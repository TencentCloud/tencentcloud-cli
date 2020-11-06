**Example 1: 查询云数据库实例续费的价格**



Input: 

```
tccli mariadb DescribeRenewalPrice --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh \
    --Period 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5b637383-8059-b0f8-3dcd-59fbdff262b6",
        "OriginalPrice": 21120,
        "Price": 21120
    }
}
```

