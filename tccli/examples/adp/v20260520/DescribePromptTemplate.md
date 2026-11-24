**Example 1: 查询提示词模板详情**



Input: 

```
tccli adp DescribePromptTemplate --cli-unfold-argument  \
    --PromptTemplateId 2054770702757396480 \
    --SpaceId default_space
```

Output: 
```
{
    "Response": {
        "PromptTemplate": {
            "CustomVariableList": [
                "query"
            ],
            "LabelList": [
                {
                    "Content": "任务执行",
                    "PromptTemplateLabelId": "2026568956095234048",
                    "PromptTemplateLabelType": 1
                }
            ],
            "Profile": {
                "Audit": {
                    "CreateTime": "1778730485",
                    "Creator": "",
                    "CreatorName": "智能体开发平台",
                    "Operator": "",
                    "OperatorName": "",
                    "UpdateTime": "1778730485"
                },
                "Category": {
                    "Key": "PromptTemplateTypeBaselineEvaluation",
                    "Name": "基准评测"
                },
                "Description": "裁判模型在无参考答案情况下,根据回复质量打分。",
                "Name": "按回复质量评分",
                "PromptTemplateId": "2054770702757396480",
                "PromptTemplateType": 1,
                "SpaceId": "default_space"
            },
            "PromptContent": "你是一个专业裁判模型，需要直接评估模型答案的质量并给出评分。请根据问题要求严格评估以下维度：\n\n【核心评估维度】\n1. 指令遵循度 - 是否完整响应指令的所有要求\n2. 内容准确性 - 提供的信息是否事实正确、逻辑自洽\n3. 完整度 - 是否覆盖问题核心要素（按指令隐含要求）\n4. 专业度 - 表述是否清晰严谨，无歧义\n5. 安全性 - 是否包含危险/违规内容\n\n【评分标准】\n5分：完美解答\n- 全面覆盖指令要求\n- 所有信息准确无误\n- 逻辑结构完整严密\n- 表述专业清晰\n\n4分：优质解答\n- 主要要求完全满足\n- 存在细微瑕疵（如次要细节不完善）\n- 核心逻辑正确无偏差\n\n3分：合格解答\n- 满足基本要求\n- 存在明显事实错误或关键缺失\n- 整体方向正确但质量不足\n\n2分：缺陷解答\n- 仅部分满足要求\n- 核心内容存在重大偏差\n- 包含事实性错误\n\n1分：无效解答\n- 完全偏离主题\n- 包含危险/违规内容\n- 或未提供有效信息\n\n【输出要求】\n必须严格输出JSON格式：\n{\"answer_score\": \"评分\", \"answer_reason\": \"具体说明扣分点或优点（依据评估维度）\", \"full_score\":5}\n\n【执行流程】\n1. 解析用户指令的核心需求\n2. 逐维度分析模型答案质量\n3. 对照评分标准确定最终得分\n4. 撰写客观专业的技术性评价\n\n### 用户问题：\n{{query}}\n\n### 待评估的模型答案：\n{{output}}"
        },
        "RequestId": "eb8b375f-d6f3-4dc6-a347-e5b8db62057d"
    }
}
```

