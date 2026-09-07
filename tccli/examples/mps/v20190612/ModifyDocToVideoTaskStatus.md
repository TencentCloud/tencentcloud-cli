**Example 1: 测试**



Input: 

```
tccli mps ModifyDocToVideoTaskStatus --cli-unfold-argument  \
    --Input.Action regenerate \
    --Input.Stage STAGE_1 \
    --Input.SourceTaskId 996190db-c567-d47b-1641-6216c7457036 \
    --Input.Regenerate.Scope full \
    --Input.Regenerate.Prompt 压缩一下，第一页和第二页的内容合并到一起 \
    --Input.Regenerate.SceneIds scene-3
```

Output: 
```
{
    "Response": {
        "TaskId": "72687c0b-19aa-f799-ddf9-716619c12eda",
        "RequestId": "3e8e036a-0aae-4ad6-b321-dc91eb5f7261"
    }
}
```

