**Example 1: Waf 会话定义查询接口**



Input: 

```
tccli waf DescribeSession --cli-unfold-argument  \
    --Domain test.com \
    --Edition clb-waf
```

Output: 
```
{
    "Res": [
        {
            "Category": "match",
            "EndMat": "&",
            "EndOffset": "-1",
            "KeyOrStartMat": "hashId",
            "Source": "get",
            "StartOffset": "-1",
            "TsVersion": "1578366436093"
        }
    ]
}
```

**Example 2: 没有设置Seesion的场景**



Input: 

```
tccli waf DescribeSession --cli-unfold-argument  \
    --Domain test.com \
    --Edition clb-waf
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "e08991ed-f8f8-4a6e-b8be-74f1a34eab5f"
    }
}
```

