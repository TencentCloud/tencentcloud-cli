**Example 1: 获取数据目录详情**

获取数据目录详情

Input: 

```
tccli wedata GetCatalog --cli-unfold-argument  \
    --CatalogName luffyshi_model
```

Output: 
```
{
    "Response": {
        "Data": {
            "Catalog": {
                "Comment": "model_test",
                "Id": "0b53ccdb-912f-4635-9b36-b2d04f2d36cb",
                "MetaOwner": {
                    "FullName": "luffyshi_model",
                    "Owner": "1290245077@qq.com",
                    "OwnerType": "user"
                },
                "Name": "luffyshi_model",
                "Operator": "1290245077@qq.com",
                "Properties": [],
                "Status": "2",
                "Type": "MODEL"
            }
        },
        "RequestId": "ef2c4e2b-8795-407e-902a-aae86b620b86"
    }
}
```

