**Example 1: ResetInstances**



Input: 

```
tccli cvd ResetInstances --cli-unfold-argument  \
    --InstanceRegion ap-shanghai \
    --IsUnbind True \
    --InstanceIds cdi-a \
    --ImageId img-a
```

Output: 
```
{
    "Response": {
        "RequestId": "rid"
    }
}
```

