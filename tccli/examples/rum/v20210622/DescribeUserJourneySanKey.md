**Example 1: 示例**



Input: 

```
tccli rum DescribeUserJourneySanKey --cli-unfold-argument  \
    --AppId 1****7 \
    --StartTime 1779167512144 \
    --EndTime 1779181912144 \
    --Platform all \
    --Filters [{"Key":"country","Op":"in","Values":["中国"]}] \
    --TopPagesPerStep 5 \
    --MinSessionThreshold 1 \
    --StartPage 商城首页 \
    --EndPage 购物车页 \
    --HasStruggle False
```

Output: 
```
{
    "Response": {
        "Result": "{\"Data\":{\"Nodes\":[],\"Links\":[],\"StepSummaries\":[],\"Stats\":{\"TotalSessions\":0,\"TotalUsers\":0,\"MaxStepLevel\":0,\"AvgPathDepth\":0,\"OverallExitRate\":0,\"StruggleSessions\":0,\"StruggleRate\":0,\"AvgStruggleScore\":0,\"IsTruncated\":false,\"HiddenNodeCount\":0,\"HiddenSessionCount\":0}}}",
        "RequestId": "c6c2468e-621d-476a-be4c-a148452851fe"
    }
}
```

