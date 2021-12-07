**Example 1: 保存告警策略**

保存告警策略

Input: 

```
tccli tcss AddEditWarningRules --cli-unfold-argument  \
    --WarningRules.0.Type IMG_VUL \
    --WarningRules.0.Switch ON \
    --WarningRules.0.BeginTime 20:00 \
    --WarningRules.0.EndTime 10:00 \
    --WarningRules.0.ControlBits 111
```

Output: 
```
{
    "Response": {
        "RequestId": "fee1bdb0-c13f-4c65-b567-8e270df211c1"
    }
}
```

