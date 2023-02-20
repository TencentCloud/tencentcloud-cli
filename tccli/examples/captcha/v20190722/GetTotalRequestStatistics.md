**Example 1: 请求和返回示例**

查询全部验证统计数据

Input: 

```
tccli captcha GetTotalRequestStatistics --cli-unfold-argument  \
    --EndTimeStr "2022-08-14 14:00" \
    --StartTimeStr "2022-05-14 10:00" \
    --Dimension "3"
```

Output: 
```
{
    "Response": {
        "RequestId": "9bc8b248-cdff-443f-8483-871f07e1e3bc",
        "Data": null,
        "CaptchaCode": 11000,
        "CaptchaMsg": ""
    }
}
```

