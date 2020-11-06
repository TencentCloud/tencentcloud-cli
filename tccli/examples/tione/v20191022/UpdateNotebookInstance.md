**Example 1: 更新Notebook实例**



Input: 

```
tccli tione UpdateNotebookInstance --cli-unfold-argument  \
    --NotebookInstanceName apitest \
    --RoleArn role_name \
    --RootAccess Enabled \
    --VolumeSizeInGB 20 \
    --LifecycleScriptsName aaa
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac85a52-fb9d-4b28-b0fa-1017b9ada1ac"
    }
}
```

