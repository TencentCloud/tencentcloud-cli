**Example 1: 获取用户在当前代码文件节点的递归最大权限**



Input: 

```
tccli wedata GetMyCodeMaxPermission --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --ResourceId 20d6fbdb-5122-49ad-a94e-ac182099e11e
```

Output: 
```
{
    "Response": {
        "Data": {
            "PermissionType": "CAN_MANAGE"
        },
        "RequestId": "a93814f7-a3b8-4d29-bb48-a6031a5b8c99"
    }
}
```

