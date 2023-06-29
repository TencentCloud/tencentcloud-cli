**Example 1: 更改合规配置**



Input: 

```
tccli sag ModifyCompliance --cli-unfold-argument  \
    --Os Windows \
    --CycleCheck 1 \
    --CycleInterval 30 \
    --FixRemind 1 \
    --IntervalUnit hour \
    --IsCustomInterval 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

