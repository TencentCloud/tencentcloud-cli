**Example 1: 查询扩容云数据库实例的价格**



Input: 

```
tccli mariadb DescribeUpgradePrice --cli-unfold-argument  \
    --InstanceId tdsql-fdpjf5zh\
    --Memory 2000\
    --Storage 20000
```

Output: 
```
{
    "Response": {
        "RequestId": "7212a9ec-a235-2144-98d4-59fbe6f14d79",
        "OriginalPrice": 720,
        "Price": 720
    }
}
```

