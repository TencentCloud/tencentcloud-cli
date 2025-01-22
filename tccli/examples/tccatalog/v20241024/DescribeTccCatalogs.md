**Example 1: 获取Tcc数据目录列表**

获取Tcc数据目录列表

Input: 

```
tccli tccatalog DescribeTccCatalogs --cli-unfold-argument  \
    --CatalogId b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1
```

Output: 
```
{
    "Response": {
        "TccCatalogSet": [
            {
                "Id": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
                "Name": "TccHiveCatalog",
                "Type": "TCC-HIVE",
                "Status": 2,
                "Operator": "3783892123",
                "CreateTime": "2024-01-01 12:00:00",
                "UpdateTime": "2024-01-01 12:00:00"
            }
        ],
        "Total": 10,
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

