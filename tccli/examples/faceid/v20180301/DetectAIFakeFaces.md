**Example 1: 不加密请求示例**



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

**Example 2: 全包体加密请求示例**



Input: 

```
tccli faceid DetectAIFakeFaces --cli-unfold-argument  \
    --Encryption.Algorithm AES-256-CBC \
    --Encryption.EncryptList EncryptionBody \
    --Encryption.CiphertextBlob qwRTgn+52FAvnfrGL1oPBsXG4FLBd42YRw \
    --Encryption.Iv vqfsaEOpGJESA== \
    --EncryptedBody v32onREKL6bk6WHOGFEjE2M6kvqybGCVTjlm
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

**Example 3: 异常示例**



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

**Example 4: 检查IP**



Input: 

```
tccli faceid DetectAIFakeFaces --cli-unfold-argument  \
    --FaceInputType 1 \
    --FaceInput data:image/*peg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aH*wgJC4n**Is**wcKDcpLDAxNDQ0Hyc5PTgy*C******2wBDAQkJCQwLDBgN*Rg*I**h*jI**jIyMjIyMjIyMjIyMjIyMjI*Mj*yM*IyMjIyMjIy*jIy*jI*M***MjI*MjIyMjL/wAARCAMAAwAD**IAAhEBAxEB/8*AHw*A*QU*AQ*BAQEA**A*AAAAAAECAwQFBgcICQoL/8QA*RA*Ag*DAwIE*wUF*AQAAA*9AQI*AA***R*hMU**E1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQ \
    --ExtraRiskInfo.Latitude 1.3048 \
    --ExtraRiskInfo.Longitude 103.8318 \
    --ExtraRiskInfo.Ip 106.55.202.186
```

Output: 
```
{
    "Response": {
        "AttackRiskDetailList": [],
        "AttackRiskLevel": "Mid",
        "ExtraInfo": {},
        "ExtraRiskResult": {
            "BlackListResult": [],
            "RiskDetailList": [
                {
                    "Type": "IpLocationMismatch"
                }
            ],
            "RiskLevel": "High",
            "Status": "Completed"
        },
        "RequestId": "5738fb6b-da7d-417f-af4d-947914e7bdc2"
    }
}
```

