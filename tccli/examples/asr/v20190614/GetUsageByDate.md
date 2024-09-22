**Example 1: 用量查询输入示例**

需要查询8月份录音识别和实时识别的用量

Input: 

```
tccli asr GetUsageByDate --cli-unfold-argument  \
    --BizNameList asr_rt asr_rec \
    --StartDate 2024-08-01 \
    --EndDate 2024-08-31
```

Output: 
```
{
    "Response": {
        "Data": {
            "UsageByDateInfoList": [
                {
                    "BizName": "asr_rt",
                    "Count": 0,
                    "Duration": 0
                },
                {
                    "BizName": "asr_rec",
                    "Count": 47,
                    "Duration": 351
                }
            ]
        },
        "RequestId": "877e8723-792b-4b4e-a8c0-57bece96b7f0"
    }
}
```

