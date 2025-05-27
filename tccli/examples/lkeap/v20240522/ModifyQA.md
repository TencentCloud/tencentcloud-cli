**Example 1: 修改问答对**

修改问答对

Input: 

```
tccli lkeap ModifyQA --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --QaId 1830995120618932160 \
    --Question 你是谁 \
    --Answer 我是您的智能助手 \
    --AttributeLabels.0.AttributeId 1830994685416869312 \
    --AttributeLabels.0.LabelIds 1830994685429452224
```

Output: 
```
{
    "Response": {
        "RequestId": "4f4843c1-8f3b-4a0b-ad7e-91b47f2b93c7"
    }
}
```

