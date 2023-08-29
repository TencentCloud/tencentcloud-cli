**Example 1: 查询标签信息**

查询标签信息

Input: 

```
tccli billing DescribeTagList --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Status": 1,
                "TagKey": "测试3",
                "UpdateTime": "2023-02-28 19:22:21"
            },
            {
                "Status": 1,
                "TagKey": "测试7",
                "UpdateTime": "2023-02-28 19:22:21"
            },
            {
                "Status": 1,
                "TagKey": "测试8",
                "UpdateTime": "2023-02-28 19:22:21"
            },
            {
                "Status": 0,
                "TagKey": "测试4"
            },
            {
                "Status": 0,
                "TagKey": "测试6"
            }
        ],
        "RecordNum": 5,
        "RequestId": "3cf36106-93e2-498d-a12f-62b3a6d9da34"
    }
}
```

