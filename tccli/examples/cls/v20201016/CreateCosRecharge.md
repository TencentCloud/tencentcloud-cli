**Example 1: 创建cos导入任务**

创建cos导入任务

Input: 

```
tccli cls CreateCosRecharge --cli-unfold-argument  \
    --TopicId ae13f7db-00b5-41ac-916e-407802axxxxx \
    --LogsetId 0af7e6bb-fc91-4ee8-ad24-1129e9cxxxxx \
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
    --ExtractRuleInfo.FilterKeyRegex.0.Key xxx \
    --ExtractRuleInfo.FilterKeyRegex.0.Regex ssss \
    --ExtractRuleInfo.UnMatchLogKey testlog \
    --ExtractRuleInfo.UnMatchUpLoadSwitch True \
    --ExtractRuleInfo.Backtracking -1
```

Output: 
```
{
    "Response": {
        "Id": "ca092608-98e8-4ad9-83c5-a6b3bbexxxxx",
        "RequestId": "dc78ee34-237b-41c7-8fcd-601a99b271f6"
    }
}
```

