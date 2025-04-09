**Example 1: 获取云存上报统计信息请求**

获取云存上报统计信息请求

Input: 

```
tccli iotvideo DescribeCsReportCountDataInfo --cli-unfold-argument  \
    --ProductId PTROMP3AOB \
    --DeviceName dfsdfsd \
    --StartTime 1743587952 \
    --EndTime 1743587952
```

Output: 
```
{
    "Response": {
        "Data": {
            "EventExceptionNum": 0,
            "EventSuccessNum": 0,
            "EventSuccessRate": "0.00%",
            "VideoExceptionNum": 0,
            "VideoSuccessNum": 0,
            "VideoSuccessRate": "0.00%"
        },
        "RequestId": "cf56eccb-3662-4eb3-9f60-ce618e749144"
    }
}
```

