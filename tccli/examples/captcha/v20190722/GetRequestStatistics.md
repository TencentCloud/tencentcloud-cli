**Example 1: 请求和返回示例**

查询单个CaptchaAppID验证数据

Input: 

```
tccli captcha GetRequestStatistics --cli-unfold-argument  \
    --CaptchaAppId "19901111" \
    --EndTimeStr "2022-08-14 14:00" \
    --StartTimeStr "2022-05-14 10:00" \
    --Dimension "3"
```

Output: 
```
{
    "Response": {
        "RequestId": "247b9e9d-abda-41a6-b067-979961aba989",
        "Data": null,
        "CaptchaCode": 11000,
        "CaptchaMsg": ""
    }
}
```

