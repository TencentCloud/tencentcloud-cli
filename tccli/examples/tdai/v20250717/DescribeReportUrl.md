**Example 1: 某个子步骤的结果作为报告输出**



Input: 

```
tccli tdai DescribeReportUrl --cli-unfold-argument  \
    --InstanceId agentins-fq9vp1md \
    --ChatId chat-x8ko90ij \
    --StreamingId strm-tyukoljn \
    --StepName 一级步骤 \
    --SubStepName 子步骤
```

Output: 
```
{
    "Response": {
        "RequestId": "4744e0fa-7827-4ae6-8eda-f5de924e1adb",
        "DownloadUrl": "https://url.download.cn/you/report"
    }
}
```

