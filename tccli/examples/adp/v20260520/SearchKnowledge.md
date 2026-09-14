**Example 1: 知识检索**



Input: 

```
tccli adp SearchKnowledge --cli-unfold-argument  \
    --AdvancedConfig.FinalRerankConfig.ModelName Youtu/youtu-reranker-llm \
    --AdvancedConfig.KbRetrievalList.0.DbRetrievalConfig.Enabled True \
    --AdvancedConfig.KbRetrievalList.0.DocRetrievalConfig.Confidence 0.2 \
    --AdvancedConfig.KbRetrievalList.0.DocRetrievalConfig.Enabled True \
    --AdvancedConfig.KbRetrievalList.0.DocRetrievalConfig.TopN 5 \
    --AdvancedConfig.KbRetrievalList.0.KbId 2067622575842400832 \
    --AdvancedConfig.KbRetrievalList.0.QaRetrievalConfig.Confidence 0.7 \
    --AdvancedConfig.KbRetrievalList.0.QaRetrievalConfig.Enabled True \
    --AdvancedConfig.KbRetrievalList.0.QaRetrievalConfig.TopN 3 \
    --AdvancedConfig.KbRetrievalList.0.RerankConfig.Enabled True \
    --AdvancedConfig.KbRetrievalList.0.RerankConfig.ModelName Youtu/youtu-reranker-llm \
    --AdvancedConfig.KbRetrievalList.0.StrategyType 0 \
    --AdvancedConfig.KbRetrievalList.0.TextToSqlModel.Alias DeepSeek-V4-Flash \
    --AdvancedConfig.KbRetrievalList.0.TextToSqlModel.HistoryLimit 0 \
    --AdvancedConfig.KbRetrievalList.0.TextToSqlModel.ModelId Deepseek/deepseek-v4-flash \
    --AdvancedConfig.KnowledgeType 1 \
    --AdvancedConfig.RecallCount 13 \
    --Input.Question 什么是肺鱼 \
    --Context.CallSource 5
```

Output: 
```
{
    "Response": {
        "KnowledgeList": [
            {
                "Confidence": 0.5791762,
                "KnowledgeType": 2,
                "RecallTypeList": [
                    2
                ],
                "ResultPayload": {
                    "GraphData": "",
                    "ImageUrlList": [],
                    "SheetInfo": ""
                },
                "ResultType": 0,
                "SimilarQuestionExtra": {
                    "Content": "",
                    "SimilarQuestionId": "0"
                },
                "SnippetProfile": {
                    "Content": "文档名：肺鱼\n文档片段：肺鱼是一类具有独特生理结构和生存能力的古老鱼类，属于硬骨鱼纲肉鳍鱼亚纲肺鱼目。它们最早出现在距今约4亿年前的泥盆纪时期，是现存最古老的鱼类之一。\n\n\n主要特征\n\n\n呼吸方式：肺鱼具有鳃和肺两个呼吸器官。在水中，它们主要通过鳃呼吸；在水体干涸时，可以利用特化的鱼鳔（称为“肺”）直接呼吸空气。\n\n\n形态结构：肺鱼的体态修长，胸鳍和腹鳍肥厚有力，可以在水底行走。它们的鳞片细小，身体呈鳗状，有助于在水草丛生的环境中灵活穿梭。\n\n\n生存能力：肺鱼能够在干旱的环境中生存。当河水干涸时，它们会钻入泥土中，形成茧状结构，通过肺部和内鼻孔呼吸，等待雨季到来。\n\n\n分布与种类\n\n\n分布：现存的肺鱼主要分布在南美洲、非洲和澳大利亚的淡水环境中。\n\n\n种类：肺鱼目包括两个主要的科——美洲肺鱼科和非洲肺鱼科。其中，澳洲肺鱼、美洲肺鱼和非洲肺鱼是较为常见的种类。\n\n\n生活习性\n\n\n食性：肺鱼以甲壳类、软体动物和蠕虫等为食，具有强大的咬合力，能够捕食带壳的无脊椎动物。\n\n\n繁殖：肺鱼的繁殖方式多样，有的种类会在水生植物中产卵，幼鱼无外鳃，发育无需经过变态；而有的种类则需要经过变态，幼鱼\n\n\n保护现状\n\n\n肺鱼因其独特的生理特性和重要的科研价值，被列入《濒危野生动植物种国际贸易公约附录Ⅰ、附录Ⅱ和附录Ⅲ》，受到国际保护。\n",
                    "DocId": "2079848099272955712",
                    "DocName": "肺鱼.txt",
                    "KbId": "2079847931153870720",
                    "KnowledgeId": "2079848160140695360",
                    "Question": "",
                    "Title": "肺鱼"
                },
                "SourceInfo": {
                    "IsBigData": false,
                    "IsShared": false,
                    "KbName": ""
                }
            }
        ],
        "TokenUsageList": [
            {
                "CompletionTokens": 0,
                "ModelName": "Youtu/youtu-embedding",
                "PromptTokens": 16,
                "TotalTokens": 16
            }
        ],
        "RequestId": "e06aa6d0-1811-480b-b21d-900bc835e6da"
    }
}
```

