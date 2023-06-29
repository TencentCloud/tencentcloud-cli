**Example 1: 查询云兔切换策略列表**

查询云兔切换策略列表

Input: 

```
tccli hasim DescribeTactics --cli-unfold-argument  \
    --TacticID 0 \
    --Name xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "12345678901",
        "Data": {
            "Total": 1,
            "List": [
                {
                    "ID": 10002,
                    "CreatedAt": "2021-07-19T16:06:54+08:00",
                    "IsAuto": 0,
                    "PingInterval": 36000,
                    "IsWeak": 1,
                    "WeakThreshold": -10,
                    "IsDelay": 1,
                    "DelayThreshold": 50,
                    "IsFake": 1,
                    "FakeIP": "www.baidu.com",
                    "FakeInterval": 60,
                    "IsNet": 1,
                    "Network": 3,
                    "IsPriorityTele": 1,
                    "PriorityTele": 1,
                    "IsBottomTele": 1,
                    "BottomTele": 1,
                    "IsBestSignal": 1,
                    "IsMove": 1,
                    "Name": "测试策略"
                }
            ]
        }
    }
}
```

