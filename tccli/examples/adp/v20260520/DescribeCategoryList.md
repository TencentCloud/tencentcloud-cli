**Example 1: 查询分类列表**

查询分类列表

Input: 

```
tccli adp DescribeCategoryList --cli-unfold-argument  \
    --KbId 2082355981171975296 \
    --FilterList.0.Name CategoryType \
    --FilterList.0.Operator 0 \
    --FilterList.0.ValueList 1 \
    --PageNumber 0 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "CategoryList": [
            {
                "CanAdd": false,
                "CanDelete": false,
                "CanEdit": false,
                "CategoryId": "2082355982908901632",
                "ChildList": [],
                "ItemCount": 0,
                "Name": "未分类"
            }
        ],
        "RequestId": "b8e226f9-8a05-4b6a-b901-9ce41fedc989"
    }
}
```

