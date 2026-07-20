**Example 1: 查询推理 API Token**

查询推理 API Token 列表。

Input: 

```
tccli teo DescribeInferenceAPITokens --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Tokens": [
            {
                "Content": "j8UaDh0ZbjW***glcGsSEEYo",
                "CreateTime": "2025-12-09T10:30:00Z",
                "Name": "MyInferenceAPIToken",
                "TokenId": "deb88f89-92b***3f3466bbb59b"
            }
        ],
        "TotalCount": 1,
        "RequestId": "b31cafd9-b573-4e52-871f-359d398b890d"
    }
}
```

