**Example 1: 用户端创建子Agent**



Input: 

```
tccli adp CreateAgent --cli-unfold-argument  \
    --AppId 2068***********2288 \
    --Agent.Profile.Name User Agent \
    --Agent.Profile.IconUrl https://cdn.xiaowei.qq.com/static/adp/agent-robot.png \
    --Agent.Profile.Role 1 \
    --Agent.Profile.Description User Agent \
    --Agent.Profile.ParentAgentId user_e55be224-3cb4-4951-abdd-3454bd70b6a1 \
    --Agent.Instructions User Agent \
    --Agent.Model.ModelId Moonshot/moonshot-v1-128k \
    --Agent.Model.Alias moonshot-v1-128k \
    --Agent.Model.ContextWordsLimit 20000 \
    --Agent.Model.InstructionsWordsLimit 20000 \
    --Agent.ToolList.0.Config.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.ToolList.0.Config.ToolId 959ea8eb-2772-4981-a92f-c4f43625b0c1 \
    --Agent.ToolList.0.Config.Description 根据输入的文本描述，智能生成与之相关的结果图（极速版） \
    --Agent.ToolList.0.Config.InputList.0.Name Image \
    --Agent.ToolList.0.Config.InputList.0.Description 参考图。Base64 和 Url 必须提供一个，如果都提供以 Url 为准。当传入Image参数时，Style和Resolution参数不生效，输出图分辨率将保持Image传入图分辨率。图片限制：单边分辨率大于128且小于2048；图片小于6M；格式支持 jpg、jpeg、png、bmp、tiff、webp。 \
    --Agent.ToolList.0.Config.InputList.0.Type 4 \
    --Agent.ToolList.0.Config.InputList.0.IsRequired False \
    --Agent.ToolList.0.Config.InputList.0.IsHidden False \
    --Agent.ToolList.0.Config.InputList.0.Input.InputType 0 \
    --Agent.ToolList.0.Config.ToolSource 0 \
    --Agent.ToolList.0.Config.IsDisabled False \
    --Agent.PluginList.0.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.PluginList.0.EnableCamRoleAuth False \
    --Agent.PluginList.0.AuthType 0 \
    --Agent.SkillList.0.SkillId f5fc841f-82fc-46ca-8152-d3bab786d52c \
    --Agent.AdvancedConfig.MaxReasoningRound 100 \
    --Kind 1
```

Output: 
```
{
    "Response": {
        "AgentId": "user_cc760218-4bb4-4c4e-b6d2-4996e212597e",
        "RequestId": "5b14e728-55b3-44cb-9d49-9dac2c96423b"
    }
}
```

**Example 2: 配置端创建主Agent**



Input: 

```
tccli adp CreateAgent --cli-unfold-argument  \
    --AppId 2068***********2288 \
    --Agent.Profile.Name My Main Agent \
    --Agent.Profile.IconUrl https://cdn.xiaowei.qq.com/static/adp/agent-robot.png \
    --Agent.Profile.Role 0 \
    --Agent.Profile.Description Agent \
    --Agent.Instructions User Agent \
    --Agent.Model.ModelId Moonshot/moonshot-v1-128k \
    --Agent.Model.Alias moonshot-v1-128k \
    --Agent.Model.ContextWordsLimit 20000 \
    --Agent.Model.InstructionsWordsLimit 20000 \
    --Agent.ToolList.0.Config.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.ToolList.0.Config.ToolId 959ea8eb-2772-4981-a92f-c4f43625b0c1 \
    --Agent.ToolList.0.Config.Description 根据输入的文本描述，智能生成与之相关的结果图（极速版） \
    --Agent.ToolList.0.Config.InputList.0.Name Image \
    --Agent.ToolList.0.Config.InputList.0.Description 参考图。Base64 和 Url 必须提供一个，如果都提供以 Url 为准。当传入Image参数时，Style和Resolution参数不生效，输出图分辨率将保持Image传入图分辨率。图片限制：单边分辨率大于128且小于2048；图片小于6M；格式支持 jpg、jpeg、png、bmp、tiff、webp。 \
    --Agent.ToolList.0.Config.InputList.0.Type 4 \
    --Agent.ToolList.0.Config.InputList.0.IsRequired False \
    --Agent.ToolList.0.Config.InputList.0.IsHidden False \
    --Agent.ToolList.0.Config.InputList.0.Input.InputType 0 \
    --Agent.ToolList.0.Config.ToolSource 0 \
    --Agent.ToolList.0.Config.IsDisabled False \
    --Agent.PluginList.0.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.PluginList.0.EnableCamRoleAuth False \
    --Agent.PluginList.0.AuthType 0 \
    --Agent.SkillList.0.SkillId f5fc841f-82fc-46ca-8152-d3bab786d52c \
    --Agent.AdvancedConfig.MaxReasoningRound 100
```

Output: 
```
{
    "Response": {
        "AgentId": "0f050c95-31b6-4d31-8c31-1fd6a6bafb4c",
        "RequestId": "c3e001ca-0abc-40cf-a16a-6e5e38f39df7"
    }
}
```

**Example 3: 配置端创建子Agent**



Input: 

```
tccli adp CreateAgent --cli-unfold-argument  \
    --AppId 2068***********2288 \
    --Agent.Profile.Name My Agent \
    --Agent.Profile.IconUrl https://cdn.xiaowei.qq.com/static/adp/agent-robot.png \
    --Agent.Profile.Role 1 \
    --Agent.Profile.Description Agent \
    --Agent.Instructions User Agent \
    --Agent.Model.ModelId Moonshot/moonshot-v1-128k \
    --Agent.Model.Alias moonshot-v1-128k \
    --Agent.Model.ContextWordsLimit 20000 \
    --Agent.Model.InstructionsWordsLimit 20000 \
    --Agent.ToolList.0.Config.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.ToolList.0.Config.ToolId 959ea8eb-2772-4981-a92f-c4f43625b0c1 \
    --Agent.ToolList.0.Config.Description 根据输入的文本描述，智能生成与之相关的结果图（极速版） \
    --Agent.ToolList.0.Config.InputList.0.Name Image \
    --Agent.ToolList.0.Config.InputList.0.Description 参考图。Base64 和 Url 必须提供一个，如果都提供以 Url 为准。当传入Image参数时，Style和Resolution参数不生效，输出图分辨率将保持Image传入图分辨率。图片限制：单边分辨率大于128且小于2048；图片小于6M；格式支持 jpg、jpeg、png、bmp、tiff、webp。 \
    --Agent.ToolList.0.Config.InputList.0.Type 4 \
    --Agent.ToolList.0.Config.InputList.0.IsRequired False \
    --Agent.ToolList.0.Config.InputList.0.IsHidden False \
    --Agent.ToolList.0.Config.InputList.0.Input.InputType 0 \
    --Agent.ToolList.0.Config.ToolSource 0 \
    --Agent.ToolList.0.Config.IsDisabled False \
    --Agent.PluginList.0.PluginId bf8ad2f3-1e5c-410a-ae81-abd7c5c14f1c \
    --Agent.PluginList.0.EnableCamRoleAuth False \
    --Agent.PluginList.0.AuthType 0 \
    --Agent.SkillList.0.SkillId f5fc841f-82fc-46ca-8152-d3bab786d52c \
    --Agent.AdvancedConfig.MaxReasoningRound 100
```

Output: 
```
{
    "Response": {
        "AgentId": "e86a4137-2a19-469f-9b47-6fd4a8c6c115",
        "RequestId": "31d23269-e98c-47df-a90d-963a00bbc4f4"
    }
}
```

