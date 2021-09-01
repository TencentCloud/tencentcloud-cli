**Example 1: 示例1**

拉取客户档案列表

Input: 

```
tccli solar DescribeCustomers --cli-unfold-argument  \
    --QueryType 0
```

Output: 
```
{
    "TotalCount": 3,
    "UserList": [
        {
            "Activity": null,
            "AudienceUserId": "645001009076244480",
            "Avatar": "http://thirdwx.qlogo.cn/mmopen/vi_32/UWsHgrAWRTszfoIWUyMBPMEI6217o8IOAHaHT2aypH0fKhHL3UkjgiaDdFt0tFj6BqzQmsiadrNu0sDFgqCho4ibA/132",
            "City": "深圳",
            "LastActiveTime": "2020-01-02 21:01:23",
            "MarkFlag": "1",
            "MonthActive": 132,
            "MonthRecommend": 0,
            "Phone": null,
            "Province": "广东",
            "RealName": null,
            "RelChannelFlag": 1,
            "Sex": 1,
            "Spread": 0,
            "WeekActive": 90,
            "WeekRecommend": 0,
            "WxCity": "深圳",
            "WxCountry": "中国",
            "WxNickname": "爱吃肉的鱼",
            "WxProvince": "广东"
        },
        {
            "Activity": null,
            "AudienceUserId": "645001013354434560",
            "Avatar": "http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTLaL0mCsCCictGKBaqU8ibHBbYR9iamDiaE2Xn3t9qMbicCE9H599bnZzcrUSgibic2l9ck2BmTwZJnYwY5Q/132",
            "City": "北京",
            "LastActiveTime": "2020-01-02 20:59:29",
            "MarkFlag": "0",
            "MonthActive": 152,
            "MonthRecommend": 0,
            "Phone": null,
            "Province": "北京",
            "RealName": null,
            "RelChannelFlag": 0,
            "Sex": 2,
            "Spread": 0,
            "WeekActive": 117,
            "WeekRecommend": 0,
            "WxCity": "昌平",
            "WxCountry": "中国",
            "WxNickname": "卷卷",
            "WxProvince": "北京"
        },
        {
            "Activity": null,
            "AudienceUserId": "649204092001980416",
            "Avatar": "http://thirdwx.qlogo.cn/mmopen/vi_32/ia9mqfl24ZtJz5iaMf2Eo6ANibzwrBAAPzW21BhVib9Ivpu1pC6lpMSTdicDCSz3JEwg6mibNegwN8qHy0s5KH4RrQiaw/132",
            "City": "西安",
            "LastActiveTime": "2020-01-02 20:12:45",
            "MarkFlag": "0",
            "MonthActive": 18,
            "MonthRecommend": 0,
            "Phone": null,
            "Province": "陕西",
            "RealName": null,
            "RelChannelFlag": 1,
            "Sex": 1,
            "Spread": 0,
            "WeekActive": 5,
            "WeekRecommend": 0,
            "WxCity": "西安",
            "WxCountry": "中国",
            "WxNickname": "",
            "WxProvince": "陕西"
        }
    ],
    "RequestId": "528cd582-5824-47c3-a9cf-c33fa07ff070"
}
```

