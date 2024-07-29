**Example 1: 调用示例-处理中**

处理中

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
        "RequestId": "0819265a-1bd7-4e0a-94a6-18463ae9b20e",
        "ResultVideoUrl": "",
        "StatusCode": "RUN",
        "StatusMsg": "处理中"
    }
}
```

**Example 2: 调用成功-任务完成**

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

