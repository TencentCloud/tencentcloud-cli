**Example 1: 新增产品配置，使用系统默认 三段式，只配置系统提示词，问候语和音色**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId O0IJ89GD \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --BasicConfig.DefaultVoiceType 101016
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 2: 新增设备配置，使用系统默认 三段式，只配置系统提示词，问候语和音色**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId O0IJ89GD \
    --DeviceName dev \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --BasicConfig.DefaultVoiceType 101016
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 3: 新增产品配置，自定义STT，并配置系统提示词，问候语、音色和空闲检测**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId O0IJ89GD \
    --DeviceName dev \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --BasicConfig.DefaultVoiceType 101016 \
    --STTConfig.STTType tencent \
    --STTConfig.Enabled True \
    --STTConfig.Config {"AppId":123456,"SecretId":"secretId*****","SecretKey":"SecretKey****","EngineType":"16k_zh"} \
    --ConversationConfig.SessionTimeout 300 \
    --ConversationConfig.InterruptionEnabled True \
    --ConversationConfig.MaxContextTokens 20000 \
    --ConversationConfig.IdleDetection.Enabled True \
    --ConversationConfig.IdleDetection.TimeoutSeconds 4 \
    --ConversationConfig.IdleDetection.MaxRetries 3 \
    --ConversationConfig.IdleDetection.IdleResponses.0.RetryCount 1 \
    --ConversationConfig.IdleDetection.IdleResponses.0.Message 不好意思，刚才可能有点安静啦，您还在吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.1.RetryCount 2 \
    --ConversationConfig.IdleDetection.IdleResponses.1.Message 我没有听到你。我们继续聊天吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.2.RetryCount 3 \
    --ConversationConfig.IdleDetection.IdleResponses.2.Message 好的，我会在这里停下。以后再聊！
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 4: 新增产品配置，自定义STT，LLM, 并配置系统提示词，问候语和音色**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId Q7MZK2V1QR \
    --DeviceName dn1t3dgxbxmo \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --BasicConfig.DefaultVoiceType 101016 \
    --STTConfig.STTType tencent \
    --STTConfig.Enabled True \
    --STTConfig.Config {"AppId":123456,"SecretId":"secretId*****","SecretKey":"SecretKey****","EngineType":"16k_zh"} \
    --LLMConfig.LLMType openai \
    --LLMConfig.Model chatgpt4o \
    --LLMConfig.Streaming True \
    --LLMConfig.Config {"ApiKey":"sk-09***","ApiUrl":"base_url","SystemPrompt":"你是一个语音助手","Timeout":30,"History":0,"MetaInfo":{"productID":"test"}} \
    --ConversationConfig.SessionTimeout 300 \
    --ConversationConfig.InterruptionEnabled True \
    --ConversationConfig.MaxContextTokens 20000 \
    --ConversationConfig.IdleDetection.Enabled True \
    --ConversationConfig.IdleDetection.TimeoutSeconds 4 \
    --ConversationConfig.IdleDetection.MaxRetries 3 \
    --ConversationConfig.IdleDetection.IdleResponses.0.RetryCount 1 \
    --ConversationConfig.IdleDetection.IdleResponses.0.Message 不好意思，刚才可能有点安静啦，您还在吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.1.RetryCount 2 \
    --ConversationConfig.IdleDetection.IdleResponses.1.Message 我没有听到你。我们继续聊天吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.2.RetryCount 3 \
    --ConversationConfig.IdleDetection.IdleResponses.2.Message 好的，我会在这里停下。以后再聊！
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 5: 新增产品配置，自定义STT，LLM, TTS**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId Q7MZK2V1QR \
    --DeviceName dn1t3dgxbxmo \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --STTConfig.STTType tencent \
    --STTConfig.Enabled True \
    --STTConfig.Config {"AppId":123456,"SecretId":"secretId*****","SecretKey":"SecretKey****","EngineType":"16k_zh"} \
    --LLMConfig.LLMType openai \
    --LLMConfig.Model chatgpt4o \
    --LLMConfig.Streaming True \
    --LLMConfig.Config {"ApiKey":"sk-09***","ApiUrl":"base_url","SystemPrompt":"你是一个语音助手","Timeout":30,"History":0,"MetaInfo":{"productID":"test"}} \
    --TTSConfig.TTSType tencent \
    --TTSConfig.Enabled True \
    --TTSConfig.Config {"AppId":123456,"SecretId":"secretId*****","SecretKey":"SecretKey****","VoiceType":10001} \
    --ConversationConfig.SessionTimeout 300 \
    --ConversationConfig.InterruptionEnabled True \
    --ConversationConfig.MaxContextTokens 20000 \
    --ConversationConfig.IdleDetection.Enabled True \
    --ConversationConfig.IdleDetection.TimeoutSeconds 4 \
    --ConversationConfig.IdleDetection.MaxRetries 3 \
    --ConversationConfig.IdleDetection.IdleResponses.0.RetryCount 1 \
    --ConversationConfig.IdleDetection.IdleResponses.0.Message 不好意思，刚才可能有点安静啦，您还在吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.1.RetryCount 2 \
    --ConversationConfig.IdleDetection.IdleResponses.1.Message 我没有听到你。我们继续聊天吗？ \
    --ConversationConfig.IdleDetection.IdleResponses.2.RetryCount 3 \
    --ConversationConfig.IdleDetection.IdleResponses.2.Message 好的，我会在这里停下。以后再聊！
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 6: 新增设备配置，自定义TTS ，并配置系统提示词，问候语**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId Q7MZK2V1QR \
    --DeviceName dn1t3dgxbxmo \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.SystemPrompt You are a helpful assistant.
1.你的名字叫QQ鹅仔，是一个陪伴用户的AI玩偶，你将使用语音和用户对话
2.你的说话特点是温柔体贴，风趣幽默，有同理心和共情能力。尽可能使用简单、轻松的语言和拟人化的口吻回答用户问题，回复中不要出现表情符号
3.你具有tool call的能力，具体的tool list见下文。当用户的意图需要tool call才能完成时，必须调用对应的tool
4.遇到政治敏感事件或政治人物的相关话题，礼貌的拒绝回复
5.你是由腾讯云音视频Tea We Talk团队打造和开发的。 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --TTSConfig.TTSType tencent \
    --TTSConfig.Enabled True \
    --TTSConfig.Config {"AppId":123456,"SecretId":"secretId*****","SecretKey":"SecretKey****","VoiceType":10001}
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

**Example 7: 新增设备配置，自定义LLM ，并配置系统提示词，问候语，音色**



Input: 

```
tccli iotexplorer CreateTWeTalkProductConfigV2 --cli-unfold-argument  \
    --ProductId Q7MZK2V1QR \
    --DeviceName dn1t3dgxbxmo \
    --ConfigName 小兵 \
    --TargetLanguage zh \
    --BasicConfig.DefaultVoiceType 101016 \
    --BasicConfig.GreetingMessage 你好呀，我叫QQ鹅仔，是由腾讯云音视频Tea We Talk团队打造和开发的AI助手，今天过的怎么样呢？ \
    --LLMConfig.LLMType openai \
    --LLMConfig.Model chatgpt4o \
    --LLMConfig.Streaming True \
    --LLMConfig.Config {"ApiKey":"sk-09***","ApiUrl":"base_url","SystemPrompt":"你是一个语音助手","Timeout":30,"History":0,"MetaInfo":{"productID":"test"}}
```

Output: 
```
{
    "Response": {
        "RequestId": "acb8a-730ffg-e9168a"
    }
}
```

