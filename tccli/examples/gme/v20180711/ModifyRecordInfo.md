**Example 1: 更新录制**

修改录制配置信息

Input: 

```
tccli gme ModifyRecordInfo --cli-unfold-argument  \
    --SubscribeRecordUserIds.SubscribeUserIds 1342 \
    --SubscribeRecordUserIds.UnSubscribeUserIds 9872 \
    --RecordMode 1 \
    --TaskId 446192236330927912 \
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

