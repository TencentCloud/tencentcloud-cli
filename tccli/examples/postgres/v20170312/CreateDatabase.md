**Example 1: 创建数据库**



Input: 

```
tccli postgres CreateDatabase --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --DatabaseName mydatabase \
    --DatabaseOwner test
```

Output: 
```
{
    "Response": {
        "RequestId": "28004847-7a50-4740-a536-19ee9db9ccc0"
    }
}
```

**Example 2: 创建指定字符编码、排序规则及字符分类的数据库**



Input: 

```
tccli postgres CreateDatabase --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --DatabaseName mydatabase \
    --DatabaseOwner test \
    --Encoding UTF8 \
    --Collate zh_CN.utf8 \
    --Ctype zh_CN.utf8
```

Output: 
```
{
    "Response": {
        "RequestId": "28004847-7a50-4740-a536-19ee9db9ccc0"
    }
}
```

