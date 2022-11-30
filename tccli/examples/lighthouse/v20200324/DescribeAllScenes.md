**Example 1: 查询全地域使用场景信息**



Input: 

```
tccli lighthouse DescribeAllScenes --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "22cef196-4013-493e-8acb-33a2cb629869",
        "TotalCount": 3,
        "SceneInfoSet": [
            {
                "SceneId": "lhsc-1ubg0exh",
                "DisplayName": "测试modify1",
                "Description": "测试测试1"
            },
            {
                "SceneId": "lhsc-h69tuf89",
                "DisplayName": "测试",
                "Description": "测试测试"
            },
            {
                "SceneId": "lhsc-1bbbtj87",
                "DisplayName": "31",
                "Description": "31"
            }
        ]
    }
}
```

