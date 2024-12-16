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
                "SceneId": "lhsc-xyz789ab",
                "DisplayName": "场景名称1",
                "Description": "场景描述1"
            },
            {
                "SceneId": "lhsc-pqr456st",
                "DisplayName": "场景名称2",
                "Description": "场景描述2"
            },
            {
                "SceneId": "lhsc-uvw123xy",
                "DisplayName": "场景名称3",
                "Description": "场景描述3"
            }
        ]
    }
}
```

