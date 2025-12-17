**Example 1: 修改数据库属性**



Input: 

```
tccli tccatalog ModifySchemaProperties --cli-unfold-argument  \
    --CatalogName testcatalog
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
        "Schema": {
            "Name": "testname"
        }
    }
}
```

