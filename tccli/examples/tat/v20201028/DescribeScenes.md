**Example 1: 查询场景**



Input: 

```
tccli tat DescribeScenes --cli-unfold-argument  \
    --SceneIds sc-12345678 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "eb973a12-71e3-4c0c-b1d8-4b863e5f5daf",
        "TotalCount": 1,
        "SceneSet": [
            {
                "SceneId": "sc-12345678",
                "SceneName": "运维场景",
                "CreatedBy": "TAT",
                "CreatedTime": "2020-11-02T02:48:11+00:00",
                "UpdatedTime": "2020-11-02T02:48:11+00:00"
            }
        ]
    }
}
```

