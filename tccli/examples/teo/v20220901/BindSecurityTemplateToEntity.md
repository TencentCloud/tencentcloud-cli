**Example 1: 将指定域名从策略模板解绑**

此方法会把已经绑定策略模板的指定域名从策略模板解绑。目前仅支持同时解绑一个域名。解绑时，支持下列选项：
1. 在规则配额允许情况下，保留当前策略。解绑时，将会为域名生成一条独立安全策略，该策略使用与当前策略模板相同的配置，其中的规则将额外占用规则配额。
2. 使用空白安全策略。使用默认空白策略，预设规则将使用默认配置，自定义规则内容将不再生效。

例如：将 a.test.com 从已有策略模板（策略模板 ID 为 temp-cuwg1hki，所属站点 ID 为 zone-2aq0e8rhu6jx ）解绑，可以参考以下示例进行解绑操作。

注意：如您选择保留当前策略配置，请确保当前站点有足够安全规则配额。剩余配额不足以支持保留当前策略时，解绑失败，域名将仍然绑定于当前策略模板上。

Input: 

```
tccli teo BindSecurityTemplateToEntity --cli-unfold-argument  \
    --ZoneId zone-2aq0e8rhu6jx \
    --Entities a.test.com \
    --TemplateId temp-cuwg1hki \
    --Operate unbind-keep-policy
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669"
    }
}
```

**Example 2: 将策略模板应用到指定域名 （绑定域名至策略模板）**

此方法会把已有策略模板应用到指定域名。支持同时绑定至多个站点的域名。

例如：将 a.test.com 和 b.example.com 域名绑定至已有策略模板（策略模板 ID 为 temp-cuwg1hki，所属站点 ID 为 zone-2aq0e8rhu6jx ），可以参考以下示例进行绑定操作。

注意：您的账号需要具有指定域名列表所归属全部站点的操作权限。

Input: 

```
tccli teo BindSecurityTemplateToEntity --cli-unfold-argument  \
    --ZoneId zone-2aq0e8rhu6jx \
    --Entities a.test.com b.example.com \
    --TemplateId temp-cuwg1hki \
    --Operate bind \
    --OverWrite True
```

Output: 
```
{
    "Response": {
        "RequestId": "09ce3d28-1119-49cd-xxxx-27cb34dac669"
    }
}
```

