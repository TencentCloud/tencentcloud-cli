**Example 1: 告警设置-更新和插入用户修改的告警设置**

告警设置-更新和插入用户修改的告警设置

Input: 

```
tccli cwp DescribeSaveOrUpdateWarnings --cli-unfold-argument  \
    --WarningObjects.0.Type 3 \
    --WarningObjects.0.DisablePhoneWarning 0 \
    --WarningObjects.0.BeginTime "00:11" \
    --WarningObjects.0.EndTime "22:33" \
    --WarningObjects.0.ControlBits "111" \
    --WarningObjects.1.Type 12 \
    --WarningObjects.1.DisablePhoneWarning 1 \
    --WarningObjects.1.BeginTime "11:11" \
    --WarningObjects.1.EndTime "11:33" \
    --WarningObjects.1.ControlBits "010"
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

