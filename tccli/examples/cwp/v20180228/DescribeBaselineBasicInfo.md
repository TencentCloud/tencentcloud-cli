**Example 1: 查询基线基础信息列表**

查询基线基础信息列表

Input: 

```
tccli cwp DescribeBaselineBasicInfo --cli-unfold-argument  \
    --BaselineName "等保二级BCXXX"
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "BaselineBasicInfoList": [
            {
                "BaselineId": 1,
                "ParentId": 1
            },
            {
                "BaselineId": 2,
                "ParentId": 2
            }
        ]
    }
}
```

