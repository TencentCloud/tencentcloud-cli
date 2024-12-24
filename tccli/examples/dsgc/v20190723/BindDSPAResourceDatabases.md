**Example 1: 绑定或解绑数据库**

批量绑定数据库实例db

Input: 

```
tccli dsgc BindDSPAResourceDatabases --cli-unfold-argument  \
    --DspaId dspa-ab43cd12 \
    --ResourceId cdb-mpe42va5 \
    --MetaType cdb \
    --BindDbItems.0.DbName test001 \
    --UnbindDbItems.0.DbName test002
```

Output: 
```
{
    "Response": {
        "DbTaskResults": [
            {
                "Result": "success",
                "ResultDescription": "update db bind status to [binded] success",
                "ErrDescription": {
                    "ErrCode": "InternalError",
                    "ErrMessage": "internal error"
                },
                "ResourceId": "cdb-mpe42va5",
                "DbName": "test001"
            }
        ],
        "RequestId": "91c7a73v-e540-4780-8b8e-74e0b65b4f1a"
    }
}
```

