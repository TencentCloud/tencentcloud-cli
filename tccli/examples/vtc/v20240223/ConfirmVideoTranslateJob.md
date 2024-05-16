**Example 1: 确认视频翻译结果**

确认视频翻译结果正例

Input: 

```
tccli vtc ConfirmVideoTranslateJob --cli-unfold-argument  \
    --JobId bEOhlL4G87lFvVmN6PnG3LAH1Kdu5tgs \
    --TranslateResults.0.SourceText 当工作或学习结果不理想， \
    --TranslateResults.0.TargetText When the result of work or study is not ideal \
    --TranslateResults.1.SourceText 甚至面临被全盘否定的情况时， \
    --TranslateResults.1.TargetText Even when faced with the situation of being completely denied \
    --TranslateResults.2.SourceText 你会如何应对？ \
    --TranslateResults.2.TargetText How would you deal with it? \
    --TranslateResults.3.SourceText 可以举例说明当时你是如何处理负面情绪， \
    --TranslateResults.3.TargetText You can give an example of how you dealt with negative emotions at that time. \
    --TranslateResults.4.SourceText 并找到解决办法的。 \
    --TranslateResults.4.TargetText And find a solution.
```

Output: 
```
{
    "Response": {
        "JobId": "bEOhlL4G87lFvVmN6PnG3LAH1Kdu5tgs",
        "RequestId": "8357c7a1-d348-4306-b744-ce6625c39fa4",
        "SessionId": "0bfda02b562d4432be1176904bbcbe68",
        "TaskId": "ecaa9680e41441399b4f29759174383f"
    }
}
```

