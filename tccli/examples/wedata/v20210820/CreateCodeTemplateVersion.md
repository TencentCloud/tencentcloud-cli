**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata CreateCodeTemplateVersion --cli-unfold-argument  \
    --ProjectId 1461767738399854592 \
    --CodeTemplateId 20250320223428932 \
    --VersionRemark qq \
    --Tasks.0.TaskId 20250327221647427 \
    --Tasks.0.MapParamList.0.Key aadd sadasd \
    --Tasks.0.MapParamList.0.Value ah \
    --Tasks.1.TaskId 20250327222417287 \
    --Tasks.1.MapParamList.0.Key aadd sadasd \
    --Tasks.1.MapParamList.0.Value ac \
    --Tasks.2.TaskId 20250321162854699 \
    --Tasks.2.MapParamList.0.Key aadd sadasd \
    --Tasks.2.MapParamList.0.Value ad \
    --OriginalParams 'aadd sadasd' \
    --NeedSubmitScheduleForTemplate True
```

Output: 
```
{
    "Response": {
        "Data": 127560,
        "RequestId": "407e402d-eacf-4acd-8d6e-54a4e812e4df"
    }
}
```

