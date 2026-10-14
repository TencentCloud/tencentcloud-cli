**Example 1: 切换大模型内容防护规则开关**

切换大模型内容防护规则开关

Input: 

```
tccli waf ModifyLLMContentRuleStatus --cli-unfold-argument  \
    --Domain clar11.waf.com \
    --Status 0 \
    --Ids 5200027927
```

Output: 
```
{
    "Response": {
        "RequestId": "bea7d605-437f-42a1-89ce-ad3208e01e1f"
    }
}
```

