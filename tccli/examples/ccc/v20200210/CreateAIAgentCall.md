**Example 1: 使用 AI Agent 发起外呼**

使用 AI Agent 发起外呼

Input: 

```
tccli ccc CreateAIAgentCall --cli-unfold-argument  \
    --Callee 008612300000000 \
    --SdkAppId 1400000000 \
    --AIAgentId 15 \
    --Callers 008601012345678 008601012345679 \
    --PromptVariables.0.Key foo \
    --PromptVariables.0.Value bar
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

