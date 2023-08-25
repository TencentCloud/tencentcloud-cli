**Example 1: 获取数据源的数据库信息**



Input: 

```
tccli dsgc DescribeDSPADataSourceDbInfo --cli-unfold-argument  \
    --DspaId dspa-001 \
    --DataSourceId test
```

Output: 
```
{
    "Response": {
        "RequestId": "20569756-56ba-4a13-b545-e1528d5cb239",
        "Items": [
            {
                "DbName": "test"
            }
        ]
    }
}
```

