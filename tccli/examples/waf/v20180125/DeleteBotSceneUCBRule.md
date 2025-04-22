**Example 1: 删除全局自定义规则**



Input: 

```
tccli waf DeleteBotSceneUCBRule --cli-unfold-argument  \
    --SceneId global \
    --Domain fgsta.qcloudwaf.com \
    --RuleId 3000004896
```

Output: 
```
{
    "Response": {
        "RequestId": "452b5c78-d94b-40f8-8058-1b45c95805bc",
        "Data": "ok"
    }
}
```

