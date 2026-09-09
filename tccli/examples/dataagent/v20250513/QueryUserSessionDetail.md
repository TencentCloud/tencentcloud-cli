**Example 1: 接口已通**



Input: 

```
tccli dataagent QueryUserSessionDetail --cli-unfold-argument  \
    --SessionId 67e0bdc1-c148-45c7-8ec5-9c8908b83932 \
    --Limit 50 \
    --Offset 0 \
    --InstanceId dataagent-haBKQxLt
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "Answer": "接口已通",
                "Context": "",
                "CreateTime": "2026-07-01 00:00:00",
                "ErrorContext": "",
                "Feedback": 0,
                "Question": "这是一条假数据，用于验证接口连通性",
                "RecordId": "fake-record-001",
                "SessionId": "67e0bdc1-c148-45c7-8ec5-9c8908b83932",
                "TraceId": "",
                "UpdateTime": "2026-07-01 00:00:00"
            }
        ],
        "RunRecord": "{\"SessionId\": \"*************************d*************\"*********************e************\"* \"******************************e*******\"****************************************e************\\\"***********************************************i********************************************************\"**\"**************SourceInfo\\\":{}}\", \"OldRecordId\": \"\", \"RecordId\": \"************************************\"}",
        "SessionId": "67e0bdc1-c148-45c7-8ec5-9c8908b83932",
        "SubAccountUin": "600000563247",
        "TotalCount": 1,
        "RequestId": "5e19effb-3897-45d7-ae73-5f2b845687db"
    }
}
```

**Example 2: 测试**



Input: 

```
tccli dataagent QueryUserSessionDetail --cli-unfold-argument  \
    --SessionId 5a905d26-a24d-47cc-a5e4-00f2d27155da \
    --Limit 1 \
    --Offset 0 \
    --InstanceId dataagent-G5XTaxnz
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "Answer": "[{\"kind\": \"run.started\", \"name\": \"\", \"status\": \"\", \"payload\": {\"question\": \"展示数据\"}, \"durationMs\": null}, {\"kind\": \"reasoning.delta\", \"name\": \"\", \"status\": \"\", \"payload\": {\"content\": \"我理解你想要查看数据，但目前会话中没有配置数据源，也没有上传任何数据文件。\\n\\n要展示数据，我需要有数据来源。你可以：\\n\\n1. **上传数据文件** - 比如 CSV、Excel 等格式的文件\\n2. **连接数据源** - 配置数据库或业务系统连接\\n3. **使用示例数据** - 我可以基于公开数据集或模拟数据为你做演示\\n\\n如果你有具体的数据分析需求，可以告诉我：\\n- 你想分析什么类型的数据？（销售、用户、产品等）\\n- 需要展示什么样的数据？（表格、图表、统计指标等）\\n- 是否需要生成报告？\\n\\n这样我可以为你创建一个演示示例来展示数据分析能力。\", \"role\": \"assistant\"}, \"durationMs\": 3423}, {\"kind\": \"run.finished\", \"name\": \"\", \"status\": \"completed\", \"payload\": {\"status\": \"completed\"}, \"durationMs\": null}]",
                "Context": "{\"KnowledgeBases\":[{\"KnowledgeBaseId\":\"klbase-TX1cUnuOLa\",\"FileIds\":[],\"SelectAllFiles\":true,\"DbTables\":[]}],\"SceneId\":\"\",\"Version\":\"2.0.1\",\"DataSourceInfo\":{}}",
                "CreateTime": "2026-07-15T11:02:25.510933+00:00",
                "ErrorContext": "",
                "Feedback": 0,
                "Model": "deepseek-v3.2",
                "Question": "展示数据",
                "RecordId": "5ad4a73d-15a8-432c-b47b-4d32ebf7ea75",
                "SessionId": "5a905d26-a24d-47cc-a5e4-00f2d27155da",
                "TraceId": "a39eb1fe-a1de-4a80-9dad-9144e85d61e7",
                "UpdateTime": "2026-07-15T11:02:31.262006+00:00"
            }
        ],
        "RunRecord": "",
        "SessionId": "5a905d26-a24d-47cc-a5e4-00f2d27155da",
        "SubAccountUin": "100047911039",
        "TotalCount": 4,
        "RequestId": "2b22a90c-2a72-498a-9552-ab97990d6819"
    }
}
```

**Example 3: 示例**



Input: 

```
tccli dataagent QueryUserSessionDetail --cli-unfold-argument  \
    --SessionId 5a905d26-a24d-47cc-a5e4-00f2d27155da \
    --Limit 100 \
    --Offset 9 \
    --InstanceId dataagent-G5XTaxnz
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "Answer": "[{\"kind\": \"run.started\", \"name\": \"\", \"status\": \"\", \"payload\": {\"question\": \"你好\"}, \"durationMs\": null}, {\"kind\": \"reasoning.delta\", \"name\": \"\", \"status\": \"\", \"payload\": {\"content\": \"你好！我是 Intellix 数据智能助手，可以帮你进行数据分析、知识检索、图表生成和报告制作等任务。\\n\\n不过我看到当前会话没有配置任何数据源，这意味着我无法直接查询数据库或业务系统。但我仍然可以帮你处理以下类型的工作：\\n\\n1. **知识库检索** - 如果你上传了文档、表格等文件，我可以从中查找信息\\n2. **示例分析和演示** - 使用公开数据集或模拟数据进行数据分析演示\\n3. **报告生成** - 创建 PDF、PPT、Excel、Word 等格式的报告\\n4. **图表制作** - 基于你提供的数据生成可视化图表\\n5. **第三方数据** - 获取股价、天气等公开信息（需要相应技能）\\n\\n请告诉我你想做什么，我会根据你的需求选择合适的方式来帮助你！\", \"role\": \"assistant\"}, \"durationMs\": 4093}, {\"kind\": \"run.finished\", \"name\": \"\", \"status\": \"completed\", \"payload\": {\"status\": \"completed\"}, \"durationMs\": null}]",
                "Context": "{\"KnowledgeBases\":[],\"SceneId\":\"\",\"Version\":\"2.0.1\",\"DataSourceInfo\":{}}",
                "CreateTime": "2026-07-15T10:01:17.148185+00:00",
                "ErrorContext": "Internal error.",
                "Feedback": 0,
                "Model": "deepseek-v3.2",
                "Question": "你好",
                "RecordId": "699908ba-f047-49c1-a8e7-c703189ea1e9",
                "SessionId": "5a905d26-a24d-47cc-a5e4-00f2d27155da",
                "TraceId": "14d16231-2f89-4be1-8e3a-cacae175e80c",
                "UpdateTime": "2026-07-15T10:01:23.509533+00:00"
            }
        ],
        "RunRecord": "",
        "SessionId": "5a905d26-a24d-47cc-a5e4-00f2d27155da",
        "SubAccountUin": "100047911039",
        "TotalCount": 10,
        "RequestId": "3a79ba02-ec0d-4059-9475-71c92a0658d2"
    }
}
```

