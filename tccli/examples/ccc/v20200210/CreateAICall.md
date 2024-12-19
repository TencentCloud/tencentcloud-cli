**Example 1: 创建AI通话示例（患者随访场景）**

本示例模拟某医院调用大模型对手术出院患者家长进行电话随访调查。

Input: 

```
tccli ccc CreateAICall --cli-unfold-argument  \
    --Callee 008612300000000 \
    --SdkAppId 1400000000 \
    --SystemPrompt 你是人民医院友善、和蔼的随访医生李医生，正在给患者小明的家长打电话。 \
    --WelcomeMessage 您好 \
    --LLMType openai \
    --Model gpt-4o-mini \
    --APIKey sk-proj-xxxxx \
    --APIUrl https://api.openai.com/v1/ \
    --VoiceType ZhiXi \
    --EndFunctionEnable True
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "SessionId": "6bb56a09278740bc80c5dc6dab783eff"
    }
}
```

