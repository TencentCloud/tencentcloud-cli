**Example 1: 创建cos导入任务**

创建cos导入任务

Input: 

```
tccli cls CreateCosRecharge --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx \
    --LogsetId xxx-xxx-xxx-xxx \
    --Name test_name \
    --Bucket test_bucket \
    --BucketRegion gz_open \
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
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx"
    }
}
```

