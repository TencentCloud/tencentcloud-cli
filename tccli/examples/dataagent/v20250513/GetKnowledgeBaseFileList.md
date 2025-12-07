**Example 1: GetKnowledgeBaseFileList**

GetKnowledgeBaseFileList

Input: 

```
tccli dataagent GetKnowledgeBaseFileList --cli-unfold-argument  \
    --InstanceId ry-123456
```

Output: 
```
{
    "Response": {
        "FileList": [
            {
                "CreateTime": "2025-05-23T11:48:22.574738",
                "FileName": "test.pdf",
                "FileSize": 100,
                "FileId": "1dsf1",
                "Type": 0,
                "Status": 1
            },
            {
                "CreateTime": "2025-05-23T11:48:22.574761",
                "FileName": "test.png",
                "FileSize": 120,
                "FileId": "1dsf2",
                "Type": 0,
                "Status": 1
            }
        ],
        "RequestId": "f7640962-9ab6-46d9-8905-f05022ff542f"
    }
}
```

**Example 2: 示例**

示例

Input: 

```
tccli dataagent GetKnowledgeBaseFileList --cli-unfold-argument  \
    --InstanceId dataagent-dfssj8sj
```

Output: 
```
{
    "Response": {
        "FileList": [],
        "RequestId": "fb3edecb-0405-4eea-b880-0bd4023dd274",
        "Total": 0
    }
}
```

