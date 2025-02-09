**Example 1: 获取AI对话调试工具配置**



Input: 

```
tccli trtc DescribeAIPlaygroundConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Base": "{\"Region\":\"ap-beijing\",\"WelcomeMessage\":\"hello\",\"InterruptMode\":0,\"InterruptSpeechDuration\":400}",
        "ASR": "{\"Language\":\"zh\",\"VadSilenceTime\":800}",
        "LLM": "{\"LLMType\":\"openai\",\"Model\":\"chat\",\"APIUrl\":\"https://api.test.com/test\",\"SystemPrompt\":\"你是对话助手\",\"APIKey\":\"eyJhbG\",\"History\":5,\"Streaming\":true}",
        "TTS": "{\"TTSType\":\"minimax\",\"Model\":\"speech\",\"ApiUrl\":\"https://api.test.com/test\",\"GroupId\":\"181066989\",\"ApiKey\":\"eyJhbG\",\"VoiceType\":\"female\",\"Speed\":1}",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

