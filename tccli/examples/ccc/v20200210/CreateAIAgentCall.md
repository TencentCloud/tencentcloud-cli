**Example 1: 使用智能体发起外呼**

使用智能体发起外呼

Input: 

```
tccli ccc CreateAIAgentCall --cli-unfold-argument  \
    --Callee 008612300000000 \
    --SdkAppId 1400000000 \
    --AIAgentId 15 \
    --Callers 008601012345678 008601012345679 \
    --Variables.0.Key foo \
    --Variables.0.Value bar \
    --Variables.1.Key dify-inputs-key \
    --Variables.1.Value value \
    --Variables.2.Key dify-inputs-user \
    --Variables.2.Value value \
    --Variables.3.Key dify-inputs-conversation_id \
    --Variables.3.Value value
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

