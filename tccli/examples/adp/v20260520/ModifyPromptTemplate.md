**Example 1: 修改提示词模版**



Input: 

```
tccli adp ModifyPromptTemplate --cli-unfold-argument  \
    --SpaceId IKxgVhsE \
    --PromptTemplateId 2120852138965976704 \
    --UpdateMask.Paths spec.name \
    --Spec.CategoryKey PromptTemplateTypeGeneral \
    --Spec.CustomVariableList message \
    --Spec.Description 通用文本表达 \
    --Spec.LabelIdList 1957634992069301385 \
    --Spec.Name 文档表达 \
    --Spec.PromptContent 帮我起草一份文档
把这段话改得更简洁
按要点整理成表格
检查这段{{message}}表述有没有歧义
```

Output: 
```
{
    "Response": {
        "RequestId": "939c3a41-a80f-4bb9-8152-5a07e14f4e48"
    }
}
```

