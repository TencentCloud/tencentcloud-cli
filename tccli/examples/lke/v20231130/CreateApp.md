**Example 1: CreateApp**



Input: 

```
tccli lke CreateApp --cli-unfold-argument  \
    --AppType knowledge_qa \
    --BaseConfig.Name 我的智能体应用 \
    --BaseConfig.Avatar https://cdn.xiaowei.qq.com/static/adp/app-default-avatar.png \
    --BaseConfig.Desc 应用描述信息 \
    --Pattern ClawAgent \
    --AgentType dialogue
```

Output: 
```
{
    "Response": {
        "AppBizId": "2049767047020830336",
        "IsCustomList": false,
        "RequestId": "7c04aa7f-45ce-41fc-91a9-0743aa65104d"
    }
}
```

