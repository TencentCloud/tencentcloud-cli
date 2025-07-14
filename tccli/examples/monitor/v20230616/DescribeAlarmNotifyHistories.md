**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor DescribeAlarmNotifyHistories --cli-unfold-argument  \
    --MonitorType MT_PROME \
    --QueryBaseTime 1734576676 \
    --QueryBeforeSeconds 172000 \
    --PageParams.PerPage 1 \
    --PageParams.PageNo 1
```

Output: 
```
{
    "Response": {
        "RequestId": "efc734bb-1caa-4a4f-a159-97115b57125a"
    }
}
```

