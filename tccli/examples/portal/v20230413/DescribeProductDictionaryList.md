**Example 1: 产品字典列表**

获取产品字典列表

Input: 

```
tccli portal DescribeProductDictionaryList --cli-unfold-argument  \
    --DictIds 2000 \
    --IncludeActivity True \
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DictId": 2000,
                "ParentId": 500,
                "Type": 1,
                "Slug": "cvm",
                "Name": "云服务器",
                "ProductOwner": [
                    "xxxxxxxxx"
                ],
                "DeveloperOwner": [
                    "xxxxxxxxx"
                ],
                "FtId": 100,
                "Weight": 2030050000,
                "IntroPageLink": "https://cloud.tencent.com/product/cvm",
                "IntroUpdateTime": "2023-07-03T09:53:44+08:00",
                "Acts": [
                    "https://cloud.tencent.com/act/pro/618season"
                ]
            }
        ],
        "RequestId": "abc",
        "Total": 1
    }
}
```

