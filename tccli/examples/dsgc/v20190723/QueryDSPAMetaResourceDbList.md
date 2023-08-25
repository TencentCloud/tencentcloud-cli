**Example 1: 示例**

获取数据库实例的全部非系统内置的DB列表。

Input: 

```
tccli dsgc QueryDSPAMetaResourceDbList --cli-unfold-argument  \
    --DspaId abc \
    --ResourceId abc \
    --ResourceRegion abc \
    --MetaType abc
```

Output: 
```
{
    "Response": {
        "DbRelationStatusItems": [
            {
                "DbName": "abc",
                "BindStatus": "abc",
                "ValidStatus": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

