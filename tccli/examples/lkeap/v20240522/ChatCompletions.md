**Example 1: 流式请求**

流式请求

Input: 

```
tccli lkeap ChatCompletions --cli-unfold-argument  \
    --Model deepseek-r1 \
    --Messages.0.Role user \
    --Messages.0.Content 你是谁 \
    --Stream True
```

Output: 
```
data:{"Choices":[{"Delta":{"Role":"assistant"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"ReasoningContent":"\n\n"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"\n\n"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"您好"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"！"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"我是"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"由"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"中国的"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"深度"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"求"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"索"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"（"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"Deep"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"Se"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"ek"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"）"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"公司"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"开发的"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"智能"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"助手"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"Deep"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"Se"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"ek"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"-R"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"1"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"。"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"如"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"您"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"有任何"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"任何"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"问题"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"，"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"我会"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"尽"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"我"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"所能"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"为您"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"提供"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"帮助"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"Content":"。"},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{},"FinishReason":"","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{},"FinishReason":"stop","Index":0}],"Created":1738697505,"Id":"60c97fbd7cfd14db07b75d56069a131f","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:[DONE]
```

**Example 2: 思维链示例**

在输出最终回答之前，模型会先输出一段思维链内容，以提升最终答案的准确性。ReasoningContent表示思维链内容，Content表示回答的内容。仅deepseek-r1推理模型支持返回ReasoningContent参数

Input: 

```
tccli lkeap ChatCompletions --cli-unfold-argument  \
    --Model deepseek-r1 \
    --Messages.0.Role user \
    --Messages.0.Content 9.11和9.8哪个大 \
    --Stream True
```

Output: 
```
data:{"Choices":[{"Delta":{"ReasoningContent":"确定"},"FinishReason":"","Index":0}],"Created":1738697628,"Id":"9c91b95dc4df49f2e9596ba07541e41a","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"ReasoningContent":"9"},"FinishReason":"","Index":0}],"Created":1738697628,"Id":"9c91b95dc4df49f2e9596ba07541e41a","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"ReasoningContent":"."},"FinishReason":"","Index":0}],"Created":1738697628,"Id":"9c91b95dc4df49f2e9596ba07541e41a","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}

data:{"Choices":[{"Delta":{"ReasoningContent":"11"},"FinishReason":"","Index":0}],"Created":1738697628,"Id":"9c91b95dc4df49f2e9596ba07541e41a","Model":"deepseek-r1","Object":"chat.completion.chunk","Usage":{"InputTokens":0,"OutputTokens":0,"TotalTokens":0}}
```

