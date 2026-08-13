**Example 1: 文件隔离**



Input: 

```
tccli csip ModifyEdrAlertIsolation --cli-unfold-argument  \
    --Targets.0.Id 1000000000000580 \
    --Targets.0.AlertId ed7ba2b9a95370778b2a589412f655aa \
    --Targets.0.AppId 260108008 \
    --Targets.0.Quuid 11c73bc2-6918-4457-88d3-1c22ef2de87b \
    --Targets.0.InstanceId ins-h0zrmp36 \
    --Targets.0.AlertSubType BRUTE_FORCE \
    --Status Isolate
```

Output: 
```
{
    "Response": {
        "RequestId": "811ebeff-18cd-4b66-a753-a8b7d30f3d58"
    }
}
```

