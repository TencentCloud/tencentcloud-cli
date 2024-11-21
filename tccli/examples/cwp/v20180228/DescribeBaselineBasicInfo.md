**Example 1: 查询基线基础信息列表**

查询基线基础信息列表

Input: 

```
tccli cwp DescribeBaselineBasicInfo --cli-unfold-argument  \
    --BaselineName "等保二级BCX"
```

Output: 
```
{
    "Response": {
        "RequestId": "ea71992a-b484-4d9c-882a-419fb6d0a5b0",
        "BaselineBasicInfoList": [
            {
                "Name": "等保二级BCX",
                "BaselineId": 1,
                "ParentId": 1
            },
            {
                "Name": "等保三级BCX",
                "BaselineId": 2,
                "ParentId": 2
            }
        ]
    }
}
```

