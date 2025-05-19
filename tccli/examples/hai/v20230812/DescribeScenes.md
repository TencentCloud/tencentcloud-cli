**Example 1: 查询场景**

查询场景

Input: 

```
tccli hai DescribeScenes --cli-unfold-argument  \
    --SceneIds sc-7ramp21e
```

Output: 
```
{
    "Response": {
        "RequestId": "82505ff0-ca36-486b-849f-50996228e838",
        "SceneSet": [
            {
                "SceneId": "sc-7ramp21e",
                "SceneName": "AI模型"
            }
        ]
    }
}
```

