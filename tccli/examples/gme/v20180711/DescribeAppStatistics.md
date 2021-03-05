**Example 1: 查询实时语音和离线语音2019-08-01至2019-08-03的用量统计**



Input: 

```
tccli gme DescribeAppStatistics --cli-unfold-argument  \
    --BizId 140000001 \
    --StartDate 2019-08-01 \
    --EndDate 2019-08-03 \
    --Services RealTimeSpeech VoiceMessage
```

Output: 
```
{
    "Response": {}
}
```

