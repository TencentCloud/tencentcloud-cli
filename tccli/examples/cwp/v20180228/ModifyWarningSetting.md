**Example 1: 告警设置-修改告警设置**

告警设置-修改告警设置

Input: 

```
tccli cwp ModifyWarningSetting --cli-unfold-argument  \
    --WarningObjects.0.BeginTime 00:00 \
    --WarningObjects.0.ControlBits 01 \
    --WarningObjects.0.DisablePhoneWarning 0 \
    --WarningObjects.0.EndTime 23:59 \
    --WarningObjects.0.Type 4
```

Output: 
```
{
    "Response": {
        "RequestId": "a2dfde02-1109-4818-8988-a4355f615442"
    }
}
```

