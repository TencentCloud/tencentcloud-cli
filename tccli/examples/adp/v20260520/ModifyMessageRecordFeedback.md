**Example 1: 对消息记录点踩**



Input: 

```
tccli adp ModifyMessageRecordFeedback --cli-unfold-argument  \
    --RecordId rcd_ecbb6143-cf9d-474b-830a-51431074df2a \
    --Score 2 \
    --ReasonList 'reason one' \
    --FeedbackContent this is a test feedback \
    --AppId 2112146673412501952
```

Output: 
```
{
    "Response": {
        "RequestId": "6d42b87a-9470-4e3b-b5fe-f5893162a7cd"
    }
}
```

