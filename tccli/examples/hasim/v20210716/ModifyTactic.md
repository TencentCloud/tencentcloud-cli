**Example 1: 创建云兔切换策略**

创建云兔切换策略

Input: 

```
tccli hasim ModifyTactic --cli-unfold-argument  \
    --Name 测试策略 \
    --IsAuto 0 \
    --PingInterval 36000 \
    --IsWeak 1 \
    --WeakThreshold -10 \
    --IsDelay 1 \
    --DelayThreshold 50 \
    --IsFake 1 \
    --FakeIP www.baidu.com \
    --FakeInterval 60 \
    --IsNet 1 \
    --Network 3 \
    --IsPriorityTele 1 \
    --PriorityTele 1 \
    --IsBottomTele 1 \
    --BottomTele 1 \
    --IsMove 1 \
    --IsBestSignal 1 \
    --TacticID 100101
```

Output: 
```
{
    "Response": {
        "RequestId": "12345678901"
    }
}
```

