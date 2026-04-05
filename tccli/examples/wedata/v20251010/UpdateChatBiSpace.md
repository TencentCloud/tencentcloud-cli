**Example 1: 更新ChatBI空间信息**



Input: 

```
tccli wedata UpdateChatBiSpace --cli-unfold-argument  \
    --Key 806111269456769024 \
    --WorkspaceId 17623497097012366 \
    --Name 示例空间_202602031114 \
    --Description 这是一个ChatBI空间 \
    --ExampleQuestionList 示例问题1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "806111269456769024"
        },
        "RequestId": "5aed85c9-0a85-4fe3-ab10-8ffb01fe0524"
    }
}
```

