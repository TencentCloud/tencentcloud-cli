**Example 1: UploadContent 示例**

开发空间-保存任务信息

Input: 

```
tccli wedata UploadContent --cli-unfold-argument  \
    --ScriptRequestInfo.FilePath /datastudio/personal/shell1234.sh \
    --ScriptRequestInfo.ProjectId 1485413914375667333 \
    --ScriptRequestInfo.Operation create \
    --ScriptRequestInfo.ExtraInfo {"taskId":"ap-shanghai|wedata-agent-sh-1257305432|/datastudio/personal/shell1234.sh"} \
    --ScriptRequestInfo.BucketName wedata-agent-sh-1257305432 \
    --ScriptRequestInfo.Region ap-shanghai \
    --ScriptRequestInfo.FileExtensionType sh \
    --RequestFromSource WEB
```

Output: 
```
{
    "Response": {
        "RequestId": "b24bf87c-c391-42cc-a41e-077f946bdff1",
        "ScriptInfo": {
            "Bucket": "wedata-agent-sh-1257305432",
            "CreateTime": "2024-04-10 10:38:15",
            "ExtraInfo": "{\"taskId\":\"ap-shanghai|wedata-agent-sh-1257305432|/datastudio/personal/shell1234.sh\"}",
            "FileExtensionType": "sh",
            "FileName": "shell1234.sh",
            "LocalPath": "/datastudio/personal/shell1234.sh",
            "LocalTempPath": null,
            "Md5Value": null,
            "Owner": "100028649733",
            "OwnerName": "demo",
            "PathDepth": null,
            "ProjectId": "100028649733",
            "Region": "ap-shanghai",
            "RemotePath": "/datastudio/personal/100028649733/shell1234.sh",
            "ResourceId": "3342446a-d046-4a97-9fe6-3c5dd9866ba4",
            "Size": null,
            "Type": "personal",
            "UpdateTime": "2024-04-10 10:38:15",
            "ZipPath": null
        }
    }
}
```

