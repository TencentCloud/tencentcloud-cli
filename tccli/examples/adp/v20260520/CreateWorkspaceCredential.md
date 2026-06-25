**Example 1: 创建沙箱工作空间**



Input: 

```
tccli adp CreateWorkspaceCredential --cli-unfold-argument  \
    --Type 2 \
    --WorkspaceId ca5b392c-67ea-459e-9edf-e7f3a47031f3 \
    --AppId 2049766565997076096 \
    --AppKey 1 \
    --ShareCode 1 \
    --UserId 1 \
    --LoginSubAccountUin 700001046587 \
    --LoginUin 700001046587
```

Output: 
```
{
    "Response": {
        "StorageType": "sandbox_e2b",
        "WorkspaceId": "ca5b392c-67ea-459e-9edf-e7f3a47031f3",
        "RequestId": "8ed8154b-3798-4b06-ba49-b4844e3c63fb"
    }
}
```

