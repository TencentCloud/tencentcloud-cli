**Example 1: 创建数据库**

创建数据库

Input: 

```
tccli cdb CreateDatabase --cli-unfold-argument  \
    --InstanceId abc \
    --DBName db_test \
    --CharacterSetName utf8
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

