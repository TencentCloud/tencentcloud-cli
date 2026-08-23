**Example 1: 示例1**



Input: 

```
tccli csip ModifyNotifySettingAk --cli-unfold-argument  \
    --Alert.0.Type AbnBehavior \
    --Alert.0.Level 4 \
    --AlertGranularity 1 \
    --Asset NewAk \
    --BeginTime 10:30:00 \
    --EndTime 16:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "2072a3f8-0b0c-476f-a156-05122d57b828"
    }
}
```

