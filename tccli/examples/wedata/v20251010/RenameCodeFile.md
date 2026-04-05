**Example 1: 代码文件重命名**

代码文件重命名

Input: 

```
tccli wedata RenameCodeFile --cli-unfold-argument  \
    --WorkspaceId workspaceId_test \
    --CodeFileId 5ce264ab-c420-4420-abd2-3eab54ac9a81 \
    --CodeFileName test1111.txt \
    --ExtensionType ide
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileId": "5ce264ab-c420-4420-abd2-3eab54ac9a81",
            "Status": true
        },
        "RequestId": "8d528e7e-d14f-4a96-b307-ec0b981af4c8"
    }
}
```

