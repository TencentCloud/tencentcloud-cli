**Example 1: 上报schema元数据**

上报schema元数据,注意数据源类型需要有schema

Input: 

```
tccli wedata ReportSchema --cli-unfold-argument  \
    --DatasourceId 62112 \
    --DatabaseName default \
    --SchemaName default_schema \
    --Description default_schema \
    --CreateTime 1751611555000 \
    --ModifiedTime 1751611555000
```

Output: 
```
{
    "Response": {
        "Guid": "2L11jgUGmdm2TdfY6qTp8w",
        "RequestId": "e6be860c-e086-4596-99f6-00d6a23e392b"
    }
}
```

