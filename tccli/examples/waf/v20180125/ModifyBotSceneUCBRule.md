**Example 1: 修改全局自定义规则**



Input: 

```
tccli waf ModifyBotSceneUCBRule --cli-unfold-argument  \
    --SceneId global \
    --Domain fgsta.qcloudwaf.com \
    --Rule.RuleType 10 \
    --Rule.Name 云图API全局白名单测试改名1 \
    --Rule.RuleId 3000004932 \
    --Rule.ValidTime 0 \
    --Rule.Timestamp 1666164720592 \
    --Rule.AdditionArg none \
    --Rule.Domain fgsta.qcloudwaf.com \
    --Rule.Rule.0.Key robots_exist \
    --Rule.Rule.0.Value.LogicValue false \
    --Rule.Rule.0.Op logic \
    --Rule.Label 友好BOT \
    --Rule.Prior 100 \
    --Rule.Appid 251197210 \
    --Rule.Action permit \
    --Rule.Desc 云图API测试场景UCB \
    --Rule.OnOff on
```

Output: 
```
{
    "Response": {
        "RequestId": "6f141b49-a21f-4a72-aa62-7fa7999e18ec",
        "Data": "ok"
    }
}
```

**Example 2: 插入全局自定义规则**



Input: 

```
tccli waf ModifyBotSceneUCBRule --cli-unfold-argument  \
    --SceneId global \
    --Domain fgsta.qcloudwaf.com \
    --Rule.RuleType 10 \
    --Rule.Name 云图API全局白名单测试1 \
    --Rule.ValidTime 0 \
    --Rule.Timestamp 1666164720592 \
    --Rule.AdditionArg none \
    --Rule.Domain fgsta.qcloudwaf.com \
    --Rule.Rule.0.Key robots_exist \
    --Rule.Rule.0.Value.LogicValue true \
    --Rule.Rule.0.Op logic \
    --Rule.Label 友好BOT \
    --Rule.Prior 100 \
    --Rule.Appid 251197210 \
    --Rule.Action permit \
    --Rule.Desc 云图API测试场景UCB \
    --Rule.OnOff on
```

Output: 
```
{
    "Response": {
        "RequestId": "bbec197a-d04f-4240-bad3-2eb8474554d4",
        "Data": "ok"
    }
}
```

**Example 3: 插入场景自定义规则**



Input: 

```
tccli waf ModifyBotSceneUCBRule --cli-unfold-argument  \
    --SceneId 3000004909 \
    --Domain fgsta.qcloudwaf.com \
    --Rule.RuleType 0 \
    --Rule.Name 云图API测试1 \
    --Rule.ValidTime 0 \
    --Rule.Timestamp 1666164720592 \
    --Rule.AdditionArg none \
    --Rule.Domain fgsta.qcloudwaf.com \
    --Rule.Rule.0.Key robots_exist \
    --Rule.Rule.0.Value.LogicValue true \
    --Rule.Rule.0.Op logic \
    --Rule.Label 疑似BOT \
    --Rule.Prior 100 \
    --Rule.Appid 251197210 \
    --Rule.Action monitor \
    --Rule.Desc 云图API测试场景UCB \
    --Rule.Id 字符串 \
    --Rule.OnOff on
```

Output: 
```
{
    "Response": {
        "RequestId": "4789cbed-1d47-44b4-adfb-f908a52f2a75",
        "Data": "ok"
    }
}
```

