**Example 1: 获取访问沙箱工具时所需要使用的访问Token**



Input: 

```
tccli ags AcquireSandboxInstanceToken --cli-unfold-argument  \
    --InstanceId a123478903213307971e7bc5793
```

Output: 
```
{
    "Response": {
        "Token": "sit_1XXJWXVbosp4ZeSSlnZBMs4wsWirZtx3Ixp1Ndz2_gQ",
        "ExpiresAt": "2025-09-12T09:00:03.116Z",
        "RequestId": "e3e03fc7-0194-436a-a179-6c5ac824e287"
    }
}
```

