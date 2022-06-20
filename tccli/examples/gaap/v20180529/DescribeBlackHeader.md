**Example 1: 查询禁用自定义header 名称列表**



Input: 

```
tccli gaap DescribeBlackHeader --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8",
        "BlackHeaders": [
            "X-Forward-For",
            "allow"
        ]
    }
}
```

