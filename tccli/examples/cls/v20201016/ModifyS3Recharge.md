**Example 1: 修改s3导入任务**



Input: 

```
tccli cls ModifyS3Recharge --cli-unfold-argument  \
    --TaskId e7a88e07-*********-92aa-2777c1333d2f \
    --TopicId 3faf22cb-*********-a3c3-c0831917aa15 \
    --Name test_del_1 \
    --TaskType 1 \
    --Enable 1 \
    --Bucket echo-***********7597 \
    --S3Region ap-so********* \
    --AccessKeyId AKIA*************CQG \
    --SecretAccessKey +AW********************************IYOxU \
    --Endpoint https://cos.example.com \
    --LogType multiline_fullregex_log \
    --Prefix csv/ \
    --Compress gzip \
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
        "RequestId": "b696bb96-e1d6-45b7-a646-db03d17c1a41"
    }
}
```

