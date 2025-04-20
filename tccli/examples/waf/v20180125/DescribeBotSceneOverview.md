**Example 1: test**



Input: 

```
tccli waf DescribeBotSceneOverview --cli-unfold-argument  \
    --Domain fgsta.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "RequestId": "dec2eb2e-cd26-4437-b3f7-899043c472d8",
        "Status": true,
        "SceneCount": 5,
        "ValidSceneCount": 4,
        "CurrentGlobalScene": {
            "SceneId": "3000004882",
            "SceneName": "登录防护场景2",
            "Priority": 1,
            "UpdateTime": 1667198325353
        },
        "CustomRuleNums": 41
    }
}
```

