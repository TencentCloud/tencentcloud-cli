**Example 1: 查看notebook生命周期脚本详情**



Input: 

```
tccli tione DescribeNotebookLifecycleScript --cli-unfold-argument  \
    --NotebookLifecycleScriptsName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "15833920455685922818",
        "NotebookLifecycleScriptsName": "abc",
        "CreateScript": "Y2Nj",
        "StartScript": "Y2Nj",
        "CreationTime": "2020-03-04 20:58:54",
        "LastModifiedTime": "2020-03-04 20:58:54"
    }
}
```

