**Example 1: 创建提示词模板**



Input: 

```
tccli adp CreatePromptTemplate --cli-unfold-argument  \
    --SpaceId IKxgVhsE \
    --Spec.CategoryKey PromptTemplateTypeGeneral \
    --Spec.CustomVariableList message \
    --Spec.Description 通用文本表达 \
    --Spec.LabelIdList 1957634992069301385 \
    --Spec.Name 文档表达提示词 \
    --Spec.PromptContent 帮我起草一份文档
把这段话改得更简洁
按要点整理成表格
检查这段{{message}}表述有没有歧义
```

Output: 
```
{
    "Response": {
        "PromptTemplateId": "2120852380708882048",
        "RequestId": "de754e25-b52b-4fdc-b225-5f0406978984"
    }
}
```

