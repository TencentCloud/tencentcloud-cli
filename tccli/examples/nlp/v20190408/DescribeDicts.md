**Example 1: 查询自定义词典列表接口示例**



Input: 

```
tccli nlp DescribeDicts --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Dicts": [
            {
                "Description": "",
                "CreateTime": "2020-05-12 06:06:34",
                "UpdateTime": "",
                "Id": "8d6c66a9b6afd22c7aeb717db07c3dfe",
                "Name": "test5"
            },
            {
                "Description": "",
                "CreateTime": "2020-05-12 03:04:03",
                "UpdateTime": "",
                "Id": "da7b62e7d7869b5304de61401190a7dc",
                "Name": "测试2"
            },
            {
                "Description": "",
                "CreateTime": "2020-05-12 05:31:41",
                "UpdateTime": "",
                "Id": "e211041f0fd6cbe3ef94d10c792f1571",
                "Name": "test4"
            }
        ],
        "RequestId": "e6c9edb5-1ec0-4292-8187-fe38f7a90c92"
    }
}
```

