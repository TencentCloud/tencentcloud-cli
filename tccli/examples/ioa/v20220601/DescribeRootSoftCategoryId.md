**Example 1: DescribeRootSoftCategoryId**



Input: 

```
tccli ioa DescribeRootSoftCategoryId --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "9ab0a926-8581-4f5b-b118-48a30418c404",
        "Data": {
            "Items": [
                {
                    "IdPath": "1",
                    "NamePath": "所有软件",
                    "Id": 1,
                    "Name": "所有软件"
                },
                {
                    "IdPath": "1.2",
                    "NamePath": "所有软件.未分类",
                    "Id": 2,
                    "Name": "未分类"
                }
            ]
        }
    }
}
```

