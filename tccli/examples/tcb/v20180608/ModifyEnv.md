**Example 1: 关闭qps按量计费**



Input: 

```
tccli tcb ModifyEnv --cli-unfold-argument  \
    --EnvId yn-1ghgrw28fa37efa1 \
    --CustomQps -1
```

Output: 
```
{
    "Response": {
        "RequestId": "c0cfa5b8-4496-4e84-8cd0-660e950547e6"
    }
}
```

**Example 2: 打开qps按量计费，qps按量计费上限为1200**



Input: 

```
tccli tcb ModifyEnv --cli-unfold-argument  \
    --EnvId yn-1ghgrw28fa37efa1 \
    --CustomQps 1200
```

Output: 
```
{
    "Response": {
        "RequestId": "09d6a0f4-7b89-485e-b02b-4b480613e7b3"
    }
}
```

