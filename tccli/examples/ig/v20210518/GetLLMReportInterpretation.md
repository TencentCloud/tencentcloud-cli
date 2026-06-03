**Example 1: 报告解读测试**



Input: 

```
tccli ig GetLLMReportInterpretation --cli-unfold-argument  \
    --PartnerId 1*******4 \
    --PartnerSecret **************a36bbdd17960b3d70e \
    --HospitalId ******38323 \
    --DialogueId 74836139-f2ca-4aba-b7de-47705aefafbd \
    --Message 帮我解读报告 \
    --ReportFileInfos.0.ReportFileUrl https://xxxx.pdf \
    --ReportFileInfos.0.ReportFileType 1 \
    --ResultType 0
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "success",
        "RequestId": "86fa7487-732f-4760-82fc-51427e84a545",
        "Data": {
            "Content": "根据您的健康报告内容，xxxxxx",
            "Think": "",
            "Sort": 0,
            "IsFinish": true,
            "IsSensitive": false,
            "IsSupportFile": true,
            "ReportInfos": [
                {
                    "ReportId": "1",
                    "IsAnalysis": true,
                    "ErrInfo": ""
                }
            ],
            "GuessQuestions": [
                {
                    "Title": "我的报告多久能出来"
                },
                {
                    "Title": "我的报告在哪查询"
                },
                {
                    "Title": "我的报告怎么打印"
                }
            ]
        }
    }
}
```

