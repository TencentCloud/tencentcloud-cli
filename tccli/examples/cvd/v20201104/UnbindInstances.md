**Example 1: UnbindInstances**



Input: 

```
tccli cvd UnbindInstances --cli-unfold-argument  \
    --BindInfos.0.InstanceId cdi-a \
    --BindInfos.0.UserId usera \
    --InstanceRegion ap-shanghai
```

Output: 
```
{
    "Response": {
        "RequestId": "rid"
    }
}
```

