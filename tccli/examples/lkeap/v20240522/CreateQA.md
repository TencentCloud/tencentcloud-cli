**Example 1: 创建问答对**

创建问答对

Input: 

```
tccli lkeap CreateQA --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --Question 你是谁 \
    --Answer 我是您的智能助手 \
    --AttributeLabels.0.AttributeId 1830994685416869312 \
    --AttributeLabels.0.LabelIds 1830994685429452224
```

Output: 
```
{
    "Response": {
        "QaId": "1830995120618932160",
        "RequestId": "28c960e9-c3ba-4a6d-be28-0d5d0dcca5ca"
    }
}
```

**Example 2: 创建无标签问答对**

创建无标签问答对

Input: 

```
tccli lkeap CreateQA --cli-unfold-argument  \
    --KnowledgeBaseId 4901991032 \
    --Question 你是谁 \
    --Answer 我是腾讯大模型知识引擎
```

Output: 
```
{
    "Response": {
        "QaId": "1831158575324892608",
        "RequestId": "a37897c3-acf5-420a-bc32-9a1da9348c13"
    }
}
```

