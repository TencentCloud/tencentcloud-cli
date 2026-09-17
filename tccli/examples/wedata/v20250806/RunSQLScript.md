**Example 1: 运行已有脚本**

传入 ScriptId 运行已保存的 SQL 脚本，运行配置（数据源、执行资源组等）取自该脚本。ScriptContent 不传则执行脚本已保存的全量内容；传入则覆盖本次运行的内容，支持原文或 Base64。本接口为异步提交，返回时任务通常仍在排队，需用 JobId 轮询 GetSQLRunResult 获取数据结果。注：本示例响应中 JobExecutionList 为 null 属历史数据，当前版本无论使用共享还是调度资源组，均会返回子查询列表（参见「免脚本临时运行」示例）。

Input: 

```
tccli wedata RunSQLScript --cli-unfold-argument  \
    --ScriptId 971c1520-836f-41be-b13f-7a6c637317c8 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": {
            "CreateTime": "2025-09-18 15:28:32",
            "EndTime": "2025-09-18 15:28:42",
            "JobExecutionList": null,
            "JobId": "6820250918152834057",
            "JobName": "SQL脚本执行任务",
            "JobType": "EXECUTOR",
            "OwnerUin": "100043952936",
            "ScriptContent": "--******************************************************************--\n--author: gordonzzhu\n--create time: 2025-01-14 21:05:48\n--可在左侧【库表】中查看数据库表信息\n--可在右上角修改数据探索的执行数据源等信息。\n--******************************************************************--\nSELECT 1;",
            "ScriptContentTruncate": false,
            "ScriptId": "0f2777fa-46d7-42cd-8b59-74ce47a375c0",
            "Status": "S",
            "TimeCost": 10000,
            "UpdateTime": "2025-09-18 15:28:42",
            "UserUin": "100028448903"
        },
        "RequestId": "08955a5f-497f-4bac-bac6-99c75191ffa7"
    }
}
```

**Example 2: 免脚本临时运行**

免脚本临时运行：不传 ScriptId，改传 ScriptConfig（DatasourceId 必填）与 ScriptContent 直接运行 SQL 片段，服务端不保存脚本。出参 ScriptId 为服务端生成的 adhoc- 前缀临时ID，可用于 ListSQLScriptRuns 反查。ScriptContent 支持原文或 Base64，本例传原文。ScriptConfig.ExecutorGroupId 未传时使用「项目管理-数据分析配置」中的执行资源组。注意：出参 JobId 为执行平台分配的任务ID，与 JobExecutionList[].JobExecutionId 配合使用；本接口为异步提交，返回时任务通常仍在排队（Status=QUEUED），需用 JobId 轮询 GetSQLRunResult 直至任务进入终态后获取数据结果。

Input: 

```
tccli wedata RunSQLScript --cli-unfold-argument  \
    --ProjectId 3327414454951170048 \
    --ScriptConfig.DatasourceId 65619 \
    --ScriptConfig.ComputeResource studio_2 \
    --ScriptConfig.ExecutorGroupId 20260107105230846836 \
    --ScriptContent show databases;
```

Output: 
```
{
    "Response": {
        "Data": {
            "JobId": "6820260903180522033",
            "JobName": "20260903-1805",
            "JobType": "EXECUTOR",
            "ScriptId": "adhoc-f085e4ba-33ef-45ec-aba2-7e6def785510",
            "ScriptContent": "show databases;",
            "Status": "QUEUED",
            "CreateTime": "2026-09-03 18:05:19",
            "UpdateTime": "2026-09-03 18:05:19",
            "EndTime": null,
            "OwnerUin": "700001893691",
            "UserUin": "700001893691",
            "TimeCost": null,
            "ScriptContentTruncate": false,
            "JobExecutionList": [
                {
                    "JobId": "6820260903180522033",
                    "JobExecutionId": "6820260903180522033_0",
                    "JobExecutionName": "Result1",
                    "ScriptContent": "show databases",
                    "Status": "QUEUED",
                    "CreateTime": "2026-09-03 18:05:19",
                    "UpdateTime": "2026-09-03 18:05:19",
                    "EndTime": null,
                    "TimeCost": null,
                    "ExecuteStageInfo": null,
                    "LogFilePath": null,
                    "ResultFilePath": null,
                    "ResultPreviewFilePath": null,
                    "SchemaInfoFilePath": null,
                    "ResultTotalCount": 0,
                    "ResultEffectCount": 0,
                    "ResultPreviewCount": 0,
                    "ContextScriptContent": null,
                    "CollectingTotalResult": false,
                    "CollectedPreviewResult": false,
                    "ScriptContentTruncate": false
                }
            ]
        },
        "RequestId": "08232e9f-cc1c-431b-b43a-d6796eba87c2"
    }
}
```

