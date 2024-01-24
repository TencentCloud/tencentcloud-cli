**Example 1: 编排空间-工作流-移动任务到工作流文件夹示例**



Input: 

```
tccli wedata MoveTasksToFolder --cli-unfold-argument  \
    --ProjectId 1522676572149563392 \
    --WorkflowId 63b3878f-0602-11ee-b7fc-043f72e73c62 \
    --TaskFolderId 1029cb2d-58f4-4400-b65a-6a3db680955f \
    --TaskIds bf8c8d93-da0b-4665-aec9-92890baa9a18
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "bf8c8d93-da0b-4665-aec9-92890baa9a18"
    }
}
```

