**Example 1: 示例**

疑似高风险攻击

Input: 

```
tccli faceid DetectAIFakeFaces --cli-unfold-argument  \
    --FaceInputType 1 \
    --FaceInput VBORw0KGgoAAAANSUhEUgAAAkYAAAI9CAYAAADfOLduAAABQ2lDQ1BJQ0MgUHJvZmlsZQAAKJFjYGASSCwoyGFhYGDIzSspCnJ3UoiIjFJgf87AziDBwMcgwqCQmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsgsz5I1BWZcn/xff7Y4dPvimWmY6lEAV0pqcTKQ/gPEyckFRSUMDIwJQLZyeUkBiN0CZIsUAR0FZM8AsdMh7DUgdhKEfQCsJiTIGci+AmQLJGckpgDZT4BsnSQk8XQkNtReEOD0CFBwNTI3LiTgVpJBSWpFCYh2zi+oLMpMzyhRcASGUKqCZ16yno6CkYGRMQMDKLwhqj/fAIcjoxgHQqzwKgODhTyQ8RQhlniBgWH3OgYG4Z8IMWUDBgYeoGn7/AsSixLhDmD8xlKcZmwEYXNvZ2Bgnfb//+dwBgZ2TQaGv9f///+9/f//v8sYGJhvMTAc+AYADqxgzYM88zoAAAA4ZVhJZk1NACoAAAAIAAGHaQAEAAAAAQAAABoAAAAAAAKgAgAEAAAAAQAAAkagAwAEAAAAAQAAAj0AAAAAi/M5dAAAQABJREFUeAHsvWd35EiSbYsIRlCkViW6pmq6Wry71vz/fzEf3n2fpufd
```

Output: 
```
{
    "Response": {
        "AttackRiskDetailList": [
            {
                "Type": "SuspectedWatermark"
            }
        ],
        "AttackRiskLevel": "High",
        "RequestId": "2dd93e6f-5121-4bac-8c64-d6ad646663d2"
    }
}
```

**Example 2: 异常示例**

图片解码失败

Input: 

```
tccli faceid DetectAIFakeFaces --cli-unfold-argument  \
    --FaceInputType 2 \
    --FaceInput AAAAHGZ0eXBtcDQyAAAAAWlzb21tcDQxbXA0MgAADXNtb292AAAAbG12aGQAAAAA2qNvttqjb7cAAB9AAACYFgABAAABAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAJ/XRyYWsAAABcdGtoZAAAAAHao2+22qNvtwAAAAEAAAAAAACYFgAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAEAAAAADwAAAAtAAAAAAACRlZHRzAAAAHGVsc3QAAAAAAAAAAQAAmBYAAAAUAAEAAAAACXVtZGlhAAAAIG1kaGQAAAAA2qNvttqjb7cAAAJYAAALaFXEAAAAAAAxaGRscgAAAAAAAAAAdmlkZQAAAAAAAAAAAAAAAENvcmUgTWVkaWEgVmlkZW8AAAAJHG1pbmYAAAAUdm1oZAAAAAEAAAAAAAAAAAAAACRkaW5mAAAAHGRyZWYAAAAAAAAAAQ
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ImageDecodeFailed",
            "Message": "图片解码失败。"
        },
        "RequestId": "0e77ad29-ad65-4901-9efc-b49a6e0a357b"
    }
}
```

