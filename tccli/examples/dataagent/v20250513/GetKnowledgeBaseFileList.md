**Example 1: GetKnowledgeBaseFileList**

GetKnowledgeBaseFileList

Input: 

```
tccli dataagent GetKnowledgeBaseFileList --cli-unfold-argument  \
    --InstanceId ry-123456 \
    --KnowledgeBaseId klbase-xjakxja
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
        "Total": 2,
        "RequestId": "f7640962-9ab6-46d9-8905-f05022ff542f"
    }
}
```

