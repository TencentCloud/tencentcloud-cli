**Example 1: 查询场景**

查询场景

Input: 

```
tccli hai DescribeScenes --cli-unfold-argument  \
    --SceneIds sc-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "82505ff0-ca36-486b-849f-50996228e838",
        "SceneSet": [
            {
                "SceneId": "sc-abcdefgh",
                "SceneName": "人工智能"
            }
        ]
    }
}
```

