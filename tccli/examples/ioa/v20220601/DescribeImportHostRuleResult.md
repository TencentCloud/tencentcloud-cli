**Example 1: 查询用户导入Host规则结果**

查询用户导入Host规则结果

Input: 

```
tccli ioa DescribeImportHostRuleResult --cli-unfold-argument  \
    --FileName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorSegmentCount": 0,
            "Items": [
                {
                    "Name": "abc",
                    "Host": "abc",
                    "ErrorSegment": [
                        "abc"
                    ],
                    "Row": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

