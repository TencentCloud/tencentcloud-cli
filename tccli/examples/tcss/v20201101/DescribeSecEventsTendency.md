**Example 1: 获取运行时安全事件新增趋势**



Input: 

```
tccli tcss DescribeSecEventsTendency --cli-unfold-argument  \
    --EndTime 2020-09-22 \
    --StartTime 2020-09-22
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "EventTendencySet": [
            {
                "EventSet": [
                    {
                        "Cnt": 1,
                        "CurTime": "2020-09-22"
                    }
                ],
                "EventType": "xx"
            }
        ]
    }
}
```

