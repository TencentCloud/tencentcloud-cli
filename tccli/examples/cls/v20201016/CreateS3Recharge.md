**Example 1: 创建s3导入任务**



Input: 

```
tccli cls CreateS3Recharge --cli-unfold-argument  \
    --TopicId 3faf22cb-*********-a3c3-c0831917aa15 \
    --Name test_del \
    --Bucket echo-************597 \
    --S3Region ap-so********* \
    --AccessKeyId AKIA**************QG \
    --SecretAccessKey +AW*************************T6OHAC4IYOxU \
    --LogType multiline_fullregex_log \
    --ExtractRuleInfo.LogRegex \s*\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2},\d{3})\]\s+\[(\w+)\]\s+([\s\S]*)\s* \
    --ExtractRuleInfo.BeginRegex \[\d+-\d+-\w+:\d+:\d+,\d+\]\s+\[\w+\]\s+.* \
    --ExtractRuleInfo.Keys timestamp \
    --ExtractRuleInfo.UnMatchUpLoadSwitch True \
    --ExtractRuleInfo.UnMatchLogKey LogParseFailure
```

Output: 
```
{
    "Response": {
        "TaskId": "e7a88e07-ed13-4dea-92aa-2777c1333d2f",
        "RequestId": "4ee40b5f-465a-4406-9055-23fc51ff359a"
    }
}
```

