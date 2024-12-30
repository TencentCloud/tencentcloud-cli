**Example 1: 创建cos导入任务**

创建cos导入任务

Input: 

```
tccli cls CreateCosRecharge --cli-unfold-argument  \
    --TopicId ae13f7db-xxxx-xxxx-916e-407802axxxxx \
    --LogsetId 0af7e6bb-xxxx-xxxx-ad24-1129e9cxxxxx \
    --Name test_name \
    --Bucket examplebucket-1250000000 \
    --BucketRegion ap-guangzhou \
    --Prefix text_prefix \
    --LogType minimalist_log \
    --Compress gzip \
    --ExtractRuleInfo.TimeKey date \
    --ExtractRuleInfo.TimeFormat %Y-%m-%d %H:%M:%S \
    --ExtractRuleInfo.Delimiter | \
    --ExtractRuleInfo.LogRegex .* \
    --ExtractRuleInfo.BeginRegex ^ \
    --ExtractRuleInfo.Keys date  content \
    --ExtractRuleInfo.AdvanceFilterRules.0.Key response_code \
    --ExtractRuleInfo.AdvanceFilterRules.0.Rule 0 \
    --ExtractRuleInfo.AdvanceFilterRules.0.Value 400|500 \
    --ExtractRuleInfo.UnMatchLogKey testlog \
    --ExtractRuleInfo.UnMatchUpLoadSwitch True \
    --ExtractRuleInfo.Backtracking -1
```

Output: 
```
{
    "Response": {
        "Id": "ca092608-98e8-xxxx-xxxx-a6b3bbexxxxx",
        "RequestId": "dc78ee34-xxxx-xxxx-8fcd-601a99b271f6"
    }
}
```

