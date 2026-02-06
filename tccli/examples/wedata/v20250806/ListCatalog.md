**Example 1: 查询类目**

查询类目

Input: 

```
tccli wedata ListCatalog --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ParentCatalogId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 0
        },
        "RequestId": "6dd2ae72-14fd-4663-b9f7-fbae527a9568"
    }
}
```

**Example 2: OpenAPI-查询Catalog**

OpenAPI-查询Catalog-空

Input: 

```
tccli wedata ListCatalog --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageCount": 0,
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 0
        },
        "RequestId": "330bc14c-4869-487f-b071-2f662b688ac7"
    }
}
```

