**Example 1: 反馈对话问题**



Input: 

```
tccli wedata FeedBackChatBiDialogue --cli-unfold-argument  \
    --Key 488bcd5a1770120494578b241a4d1 \
    --FeedbackRating THUMBS_DOWN \
    --FeedbackContent 日期/时间错误 \
    --Comment 事件异常 \
    --WorkspaceId 17678671667189298 \
    --RoomKey 803627528827023360
```

Output: 
```
{
    "Response": {
        "Data": {
            "Id": "6324",
            "Key": "488bcd5a1770120494578b241a4d1",
            "OwnerUin": "700002164619",
            "AppId": "260073493",
            "WorkspaceId": "17678671667189298",
            "Owner": "700002164619",
            "CreatedBy": "700002164619",
            "CreatedOn": "1770120494578",
            "ModifiedBy": "700002164619",
            "ModifiedOn": "1770124099675",
            "RoomKey": "803627528827023360",
            "ChatTaskKey": "04e8687617701204945594888e03b",
            "DialogueDisplayKey": "dialogue_1770120494575",
            "Query": "查询电影数量",
            "QueryContent": "",
            "ResultContent": "{\"dialogueId\":6324,\"traceId\":\"4c96a915-960a-4235-9239-f8c1b0143b2a\",\"taskKey\":\"04e8687617701204945594888e03b\",\"dialogueKey\":\"488bcd5a1770120494578b241a4d1\",\"roomKey\":\"803627528827023360\",\"workspaceId\":\"17678671667189298\",\"connectionId\":\"connectionId_588ca965_4c96a915-960a-4235-9239-f8c1b0143b2a\",\"chatType\":\"CHAT_QUERY_DATA\",\"code\":0,\"costTime\":86331,\"timestamp\":1770120580920,\"data\":{\"questionUnderstandingStepData\":{\"timestamp\":1770120504113,\"extraData\":{\"chatQueryUiStep\":\"think\"},\"status\":\"SUCCESS\",\"result\":{\"intentType\":\"data_question\",\"route\":\"standard_query\",\"understandingResult\":{\"originalQuestion\":\"查询电影数量\",\"understandingContent\":\"用户询问“查询电影数量”，这是一个数据查询问题，意图是获取数据库中电影（movie）的总数量。问题清晰明确，不涉及歧义。\"}}},\"tableSelectionStepData\":{\"timestamp\":1770120506999,\"extraData\":{\"chatQueryUiStep\":\"think\"},\"status\":\"SUCCESS\",\"result\":{\"selectedTables\":[{\"tableName\":\"`DataLakeCatalog`.`chatbi`.`movie_info`\",\"tableKey\":\"0f9ba31217694077336760562221e\"}],\"noTable\":false,\"tableSelectedReason\":\"问题为查询电影数量，movie_info 表包含电影ID字段，可直接统计，无需关联其他表。\"}},\"sqlExecutionStepData\":{\"timestamp\":1770120577679,\"extraData\":{\"chatQueryUiStep\":\"think\"},\"status\":\"SUCCESS\",\"result\":{\"sqlExecutedStatement\":\"SELECT  COUNT(*) AS movie_count\\nFROM    `DataLakeCatalog`.`chatbi`.`movie_info`;\",\"originalSqlExecutedStatement\":\"SELECT COUNT(*) AS movie_count FROM `DataLakeCatalog`.`chatbi`.`movie_info`;\",\"executionPlan\":\"统计电影信息表中的电影总数。\",\"resultLink\":\"/sqlresult/20260203/sql_res_488bcd5a1770120494578b241a4d1_4648e8b7.json\",\"originalResultLink\":\"/sqlresult/20260203/sql_res_488bcd5a1770120494578b241a4d1_6dcd8493.json\",\"retryCount\":0,\"executionStage\":2,\"sqlModified\":false}},\"finalAnswerStepData\":{\"timestamp\":1770120579099,\"status\":\"SUCCESS\",\"result\":{\"content\":\" 查询结果显示，当前数据库中共有 100 部电影。\"}},\"recommendQuestionStepData\":{\"timestamp\":1770120580901,\"extraData\":{},\"code\":0,\"status\":\"SUCCESS\",\"result\":{\"aiRecommendQuestions\":[\"查询各类电影的数量分布情况，并按数量降序排列\",\"查看最近一年上映的电影有哪些？\",\"分析电影的平均评分与预算的关系\"],\"canRefresh\":true}}},\"extraData\":{\"sessionId\":\"f0ff8941-17ef-4a7c-8592-2636a0921c10\"},\"isCancel\":false}",
            "Status": "FINISHED",
            "ChatType": "CHAT_QUERY_DATA",
            "FeedbackRating": "THUMBS_DOWN",
            "FeedbackContent": [
                "日期/时间错误"
            ],
            "ReviewRequestStatus": "REVIEWED",
            "Comment": "事件异常"
        },
        "RequestId": "2871c31f-7292-480b-b6a1-d6d1f76675ac"
    }
}
```

