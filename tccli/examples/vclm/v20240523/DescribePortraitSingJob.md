**Example 1: 调用成功-任务完成**

任务完成

Input: 

```
tccli vclm DescribePortraitSingJob --cli-unfold-argument  \
    --JobId 1199964964965990400
```

Output: 
```
{
    "Response": {
        "JobId": "1199964964965990400",
        "RequestId": "2564192f-1af0-4d1d-ac92-fac0f5844f73",
        "ResultVideoUrl": "https://***.mp4",
        "StatusCode": "DONE",
        "StatusMsg": "处理完成"
    }
}
```

