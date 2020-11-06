**Example 1: 查询自定义词库的词条接口示例**



Input: 

```
tccli nlp DescribeWordItems --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --DictId udf-066edc3449
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "RequestId": "2e064c2d-ee8f-4138-b153-c6b7656bf29b",
        "WordItems": [
            {
                "Text": "男朋友",
                "Pos": "",
                "CreateTime": "2020-08-04 20:51:51"
            },
            {
                "Text": "理想型",
                "Pos": "",
                "CreateTime": "2020-08-04 20:51:52"
            },
            {
                "Text": "舒畅",
                "Pos": "",
                "CreateTime": "2020-08-04 20:51:53"
            }
        ]
    }
}
```

