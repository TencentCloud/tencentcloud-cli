**Example 1: 创建Notebook生命周期脚本**



Input: 

```
tccli tione CreateNotebookLifecycleScript --cli-unfold-argument  \
    --NotebookLifecycleScriptsName abc \
    --CreateScript YWJj \
    --StartScript YWJj
```

Output: 
```
{
    "Response": {
        "RequestId": "d1bf5910-d5c8-443d-80f1-15fd8adce51e",
        "NotebookLifecycleScriptsName": "abc"
    }
}
```

