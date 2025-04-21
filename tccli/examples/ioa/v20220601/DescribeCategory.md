**Example 1: DescribeCategory**



Input: 

```
tccli ioa DescribeCategory --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 6 \
    --ParentId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "ebf73857-8fd3-4a19-a371-042e40551a03",
        "Data": {
            "Page": {
                "PageSize": 0,
                "PageNum": 0,
                "PageCount": 0,
                "Total": 4
            },
            "SoftCategoryChildrenList": [
                {
                    "CategoryId": 2,
                    "Count": 0,
                    "ParentId": 1,
                    "Leaf": 0,
                    "Sort": 2,
                    "Name": "未分类",
                    "IdPath": "1.2"
                },
                {
                    "CategoryId": 3,
                    "Count": 0,
                    "ParentId": 1,
                    "Leaf": 0,
                    "Sort": 0,
                    "Name": "testb",
                    "IdPath": "1.3"
                },
                {
                    "CategoryId": 4,
                    "Count": 0,
                    "ParentId": 1,
                    "Leaf": 0,
                    "Sort": 0,
                    "Name": "ke",
                    "IdPath": "1.4"
                },
                {
                    "CategoryId": 5,
                    "Count": 0,
                    "ParentId": 1,
                    "Leaf": 0,
                    "Sort": 0,
                    "Name": "字符串",
                    "IdPath": "1.5"
                }
            ]
        }
    }
}
```

