**Example 1: 创建下发策略**



Input: 

```
tccli fwm CreateStrategy --cli-unfold-argument  \
    --Product enterprise_sg \
    --ReceiveAccount 100011616646 \
    --PreStrategy.0.GroupId fwmrg-sygzqi8x \
    --PreStrategy.0.Sequence 1 \
    --PreStrategy.1.GroupId fwmrg-5gxybcnr \
    --PreStrategy.1.Sequence 2 \
    --PostStrategy.0.GroupId fwmrg-6wq0b6j0 \
    --PostStrategy.0.Sequence 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0517848f-e4bf-419e-a26a-724289d0b9ea"
    }
}
```

