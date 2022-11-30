**Example 1: 查询使用场景**



Input: 

```
tccli lighthouse DescribeScenes --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SceneSet": [
            {
                "SceneId": "lhsc-abcd1235",
                "DisplayName": "测试1",
                "Description": "测试测试1"
            }
        ],
        "TotalCount": 1,
        "RequestId": "4836c744-4de2-44c0-ba5c-096ccf8c923f"
    }
}
```

