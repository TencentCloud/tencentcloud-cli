**Example 1: 创建工作流中任务目录接口**



Input: 

```
tccli wedata CreateTaskFolder --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --FolderName we3 \
    --WorkflowId f13295ee-eac1-406a-ad8f-f4652e1386ef \
    --ParentFolderId  \
    --TaskNodeType GENERAL
```

Output: 
```
{
    "Response": {
        "Data": "f09452b7-de8b-42fc-b5bc-b5f247b66f38",
        "RequestId": "e3e0db80-b1e4-4a86-9f36-501485d4c848"
    }
}
```

