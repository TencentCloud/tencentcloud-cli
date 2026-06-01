**Example 1: 用户列表**



Input: 

```
tccli tchousex DescribeRoleV2 --cli-unfold-argument  \
    --ApiType RoleList \
    --InstanceId instance-vzarb8go \
    --Limit 10 \
    --Offset 0 \
    --UserToken eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NfdXVpZCI6ImYwNjFlYThhLTU3MzgtNDVkNi05NWU2LWNlNzJkNGFjYWY2YSIsImF1dGhvcml6ZWQiOnRydWUsImNlcnQiOiJ7XCJUbXBTZWNyZXRJZFwiOlwiQUtJRGNGLTlOYnVYZnZmX3FrOVUwUlpSU1haYy1feV85c3BzdDZEaEU2cjNGOTkwbDZackU2Ym9HMTJsMW1BczBJU2RcIixcIlRtcFNlY3JldEtleVwiOlwiRXVWbEI3SFl1Z05yRVNFSE5pTVNzR001WEhZVGs2QzJVWHNpb1BCd25HQT1cIixcIlRva2VuXCI6XCI2aHU5QVFpSkxxMzZwNjhIcUpLaXFmYzRNSU1qYTJtYWEyMDE2YmZkYWIyNGI3N2RmMjA4MTFkZWZiZThlN2RjTVc3UEtjT2JxSkZPb1hGUWhxdTRYX0trS0hBdjQ4YUxtM3lBUTcyUUdxUVR4ZHdQZUZuUjRzX3ZyVkpMcTJpdjZ1dWhTeFF4NUJ1a0MtSzNROXpPU3hHZ09VRWhZeV90M3ZMMDdVSHVGUnpTOEEtMHowR3B6bm4tOEVEU0JtMGNCeHVVdnhTOU1UeWFnZThBLVpyREg5a2QxSnMwUjdhZDRlbHFpRW9zbEljVm5oZjNOVUJLVk5OU3JBQWdEWVEwbFFFRm9XeXBiT0wtcFY0VGZxYWlvSGVUeTAtZFIyZnk4TUU0aEpfZlRUNWs4QU56NUtoVl90UHU5aHhPUHVHemktbEVxd09MN0F3LVllLVhXdnpVR2tXUGhDZ2ZuUE1pbU1KMkVIVGdYVGdPN0hGSEhRaE9tOV9tdzFxZ2JMWUFwSmJzeXBhVmlrVUpRQTZwUHJzd1B3XCJ9IiwiaW5zdGFuY2VfaWQiOiJpbnN0YW5jZS12emFyYjhnbyIsInVzZXJfbmFtZSI6IjEwMDAwNjgxMTgxOCJ9.NA_OL8ZsxWO7arsSY_Y3F3G5QMagf0KpFYuqoKx3T9Q
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "24a6ffa9-5dff-4330-b75e-e346d90b7c37",
        "ReturnData": "{\"TotalCount\":5,\"DescribeRoleV2List\":[{\"RoleId\":225,\"RoleName\":\"Admin\",\"Description\":\"系统管理员\",\"UserCount\":7,\"CreateTime\":\"2025-09-16T16:10:42+08:00\",\"CreateBy\":\"100018664007\",\"IsRemain\":true},{\"RoleId\":356,\"RoleName\":\"role_2\",\"Description\":\"测试\",\"UserCount\":2,\"CreateTime\":\"2025-10-28T10:46:52+08:00\",\"CreateBy\":\"100043935658\",\"IsRemain\":false},{\"RoleId\":341,\"RoleName\":\"role3\",\"Description\":\"测试测试\",\"UserCount\":3,\"CreateTime\":\"2025-10-16T20:00:19+08:00\",\"CreateBy\":\"100006294444\",\"IsRemain\":false},{\"RoleId\":338,\"RoleName\":\"role2\",\"Description\":\"测试测试666\",\"UserCount\":3,\"CreateTime\":\"2025-10-13T11:45:39+08:00\",\"CreateBy\":\"100043935658\",\"IsRemain\":false},{\"RoleId\":227,\"RoleName\":\"role_1\",\"Description\":\"\",\"UserCount\":2,\"CreateTime\":\"2025-09-19T15:22:50+08:00\",\"CreateBy\":\"100043935658\",\"IsRemain\":false}]}"
    }
}
```

