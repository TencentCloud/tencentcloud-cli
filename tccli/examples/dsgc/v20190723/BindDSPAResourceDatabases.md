**Example 1: 示例**

批量绑定数据库实例db

Input: 

```
tccli dsgc BindDSPAResourceDatabases --cli-unfold-argument  \
    --DspaId abc \
    --ResourceId abc \
    --MetaType abc \
    --BindDbItems.0.DbName abc \
    --UnbindDbItems.0.DbName abc
```

Output: 
```
{
    "Response": {
        "DbTaskResults": [
            {
                "Result": "abc",
                "ResultDescription": "abc",
                "ErrDescription": {
                    "ErrCode": "abc",
                    "ErrMessage": "abc"
                },
                "ResourceId": "abc",
                "DbName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

