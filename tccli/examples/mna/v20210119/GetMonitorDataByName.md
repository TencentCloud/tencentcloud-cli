**Example 1: 根据DeviceName（test0916）获取监控数据文件下载链接**



Input: 

```
tccli mna GetMonitorDataByName --cli-unfold-argument  \
    --DeviceName test0916 \
    --BeginTime 1757865600 \
    --EndTime 1758544927
```

Output: 
```
{
    "Response": {
        "FilePath": "https://mpacc-1258344699.cos.ap-shanghai.myqcloud.com/statistics/test0916-2025-09-15%2000%3A00-2025-09-22%2020%3A42.xlsx?x-cos-security-token=jbHT6Au3IyqAzImDJ7OdTkQ4p9KEM7na6ee3e51e8ec37e302783895fd151f13bZ7AsI8iUE1m3lkPZvh4nES34VFP_i5h8Rzc-ktTG4qsVkp4OA2R-eYxnBlRvLSzBFnBXkp-3_AXZPcJVZl9BnR3nmGzyHVuy0pdQXvgFonpYl9R8zg8PmcrKg5xn60WXalm0xkYbEeZYNFFWaUWTI_h0BX4vbm3XxDp-GQ6Q_OADCi_H4kT-uakfDE6fnt8SrP7qlHVLTfLCOTSqvNoaT4sjXmIaR356TIOZQ5D64TN9ifsHu3QFyAHkbZFTwMzmDOHaJEY1OTwDmFO9S3SosA&q-sign-algorithm=sha1&q-ak=AKID-oMDWX77h9wxXqhV_3kJcRLY4WsmvmWtWtvi8wVyjzOZl8sJnnhW0Y77Hra_tbJy&q-sign-time=1758545263%3B1758548863&q-key-time=1758545263%3B1758548863&q-header-list=host&q-url-param-list=x-cos-security-token&q-signature=26276e2bab1c468111b665d2d2a491643dda356e",
        "RequestId": "999228ed-2113-4431-8162-de82508419fd"
    }
}
```

