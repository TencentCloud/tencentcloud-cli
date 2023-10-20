**Example 1: 拖拽文件夹**



Input: 

```
tccli oceanus ModifyFolder --cli-unfold-argument  \
    --SourceFolderId folder-aaaaaaaa \
    --TargetFolderId folder-bbbbbbbb \
    --FolderName  \
    --FolderType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

**Example 2: 修改文件夹名**



Input: 

```
tccli oceanus ModifyFolder --cli-unfold-argument  \
    --SourceFolderId folder-aaaaaaaa \
    --TargetFolderId  \
    --FolderName joylyutest \
    --FolderType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5d5a201f-0a3d-485f-a82f-3c73ccca348a"
    }
}
```

