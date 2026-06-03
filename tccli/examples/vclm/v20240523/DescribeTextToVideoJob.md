**Example 1: 调用示例**



Input: 

```
tccli vclm DescribeTextToVideoJob --cli-unfold-argument  \
    --JobId 1431196242095972352
```

Output: 
```
{
    "Response": {
        "Duration": "5.041",
        "ErrorCode": "",
        "ErrorMessage": "",
        "FinalUnitDeduction": "2",
        "ResultVideoUrl": "https://cos.ap-guangzhou.tencentcos.cn/xxx.mp4",
        "Status": "DONE",
        "VideoId": "868596973359087678",
        "RequestId": "ac6b24b6-c5bf-48fe-975d-57ae9d84e084"
    }
}
```

