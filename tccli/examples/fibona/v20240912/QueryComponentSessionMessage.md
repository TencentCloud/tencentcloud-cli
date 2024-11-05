**Example 1: 查询成功**

测试查询结果

Input: 

```
tccli fibona QueryComponentSessionMessage --cli-unfold-argument  \
    --UserGroupUniqueID rum-qZsJlN6****5QJEO** \
    --FAPPID eeadd2a631a83aa9 \
    --TriggerID 16 \
    --CustomIdentify test
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "Dialog": {
                "CreatedAt": "2024-10-11T15:00:32.971+08:00",
                "ID": 3221,
                "Messages": [
                    {
                        "Abort": false,
                        "CreatedAt": "2024-10-11T15:03:53.027+08:00",
                        "Error": "",
                        "Feedback": [],
                        "ID": 7514,
                        "LLMTypeID": 12,
                        "ModelName": "hunyuan-pro",
                        "Origin": "{\"reply\":[{\"content\":\"“test”是一个英文单词，它可以用作名词或动词。以下是关于“test”的一些基本解释和用法：\\n\\n### 作为名词\\n\\n1. **测试**：指对某事物进行检验、试验，以确定其性能、质量、准确性等。\\n2. **试题**：在教育领域，常用来指考试或测验中的题目。\\n\\n### 作为动词\\n\\n1. **测试**：对某物或某人进行检验、试验，以评估其性能、能力或其他特性。\\n2. **考验**：指通过某种方式来检验或验证某人的品质、能力或决心。\\n\\n### 例句\\n\\n1. 我们正在进行一项新软件的测试。（名词用法）\\n2. 老师给了我们一个很难的测试题。（名词用法）\\n3. 我们需要测试一下这个新设备的性能。（动词用法）\\n4. 这次经历对他来说是一次严峻的考验。（动词用法）\\n\\n“test”这个词在日常生活、学习、工作等多个领域都有广泛的应用。如果你需要更具体的帮助，请提供更多上下文，我会尽力为你提供详细的解释和示例。\",\"note\":\"\",\"tag\":\"llm\"}]}",
                        "PromptID": 1694,
                        "PromptName": "",
                        "Role": "assistant",
                        "TraceID": "5478e40d-b2d7-4609-b95b-a818bf2e4869",
                        "WorkflowInfo": "{\"tool_calls\":[],\"tool_configs\":[],\"use_models\":[\"hunyuan-pro\"]}"
                    },
                    {
                        "Abort": false,
                        "CreatedAt": "2024-10-11T15:03:53.026+08:00",
                        "Error": "",
                        "Feedback": [],
                        "ID": 7513,
                        "LLMTypeID": 12,
                        "ModelName": "hunyuan-pro",
                        "Origin": "{}",
                        "PromptID": 1694,
                        "PromptName": "test",
                        "Role": "user",
                        "TraceID": "5478e40d-b2d7-4609-b95b-a818bf2e4869",
                        "WorkflowInfo": "{\"tool_calls\":[],\"tool_configs\":[],\"use_models\":[]}"
                    }
                ],
                "Title": "测试信息汇总"
            }
        },
        "JSONStrPaths": [
            "Data.Dialog.Messages.Origin",
            "Data.Dialog.Messages.WorkflowInfo"
        ],
        "Msg": "success",
        "RequestId": "518f67cf-50c1-4441-b2bd-14342df939b3"
    }
}
```

