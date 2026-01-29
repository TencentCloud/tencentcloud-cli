**Example 1: 更新录制**

修改录制配置信息

Input: 

```
tccli gme ModifyRecordInfo --cli-unfold-argument  \
    --SubscribeRecordUserIds.SubscribeUserIds 44619223 \
    --SubscribeRecordUserIds.UnSubscribeUserIds 44619224 \
    --RecordMode 1 \
    --TaskId 446192236330927940 \
    --BizId 3400352518
```

Output: 
```
{
    "Response": {
        "RequestId": "h9167d24-a2c6-1125-a5bd-5c023ba721c2"
    }
}
```

