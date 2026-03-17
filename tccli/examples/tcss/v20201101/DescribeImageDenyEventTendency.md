**Example 1: 查询镜像拦截事件趋势**



Input: 

```
tccli tcss DescribeImageDenyEventTendency --cli-unfold-argument  \
    --EndTime 2021-05-01 \
    --StartTime 2021-05-07
```

Output: 
```
{
    "Response": {
        "AlarmList": [
            {
                "Date": "2020-09-22",
                "EventCount": 0
            }
        ],
        "DenyList": [
            {
                "Date": "2020-09-22",
                "EventCount": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

