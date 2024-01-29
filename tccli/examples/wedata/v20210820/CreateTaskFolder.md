**Example 1: 创建工作流中任务目录接口**



Input: 

```
tccli wedata CreateTaskFolder --cli-unfold-argument  \
    --ProjectId 1522676572149563392 \
    --FolderName FFFOOOLLLDDDEERR \
    --ParentFolderId 6cccb832-b76a-11ed-b7fc-043f72e73c62 \
    --WorkflowId 63b3878f-0602-11ee-b7fc-043f72e73c62
```

Output: 
```
{
    "Response": {
        "Data": "277e97b2-8475-11ee-bfeb-b8cef68a6637",
        "RequestId": "7d1d9f10-fb66-40c3-b704-5e174ebc95dd"
    }
}
```

