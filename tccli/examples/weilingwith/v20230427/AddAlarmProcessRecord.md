**Example 1: 添加告警处理记录**

成功响应

Input: 

```
tccli weilingwith AddAlarmProcessRecord --cli-unfold-argument  \
    --RecordSet.0.Id 7fd854c2-e9c4-4347-b0a6-3bf5a80ac3f6 \
    --RecordSet.0.Processor 12 \
    --RecordSet.0.ProcessTime 1693417958 \
    --RecordSet.0.ProcessType add_record \
    --WorkspaceId 1016 \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "1f4ae18a-6a8e-477f-9335-d59546768e93",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

