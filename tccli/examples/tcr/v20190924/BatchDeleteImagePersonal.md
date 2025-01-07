**Example 1: 个人版镜像仓库批量删除Tag**



Input: 

```
tccli tcr BatchDeleteImagePersonal --cli-unfold-argument  \
    --RepoName nicokang/golang \
    --Tags 1 2
```

Output: 
```
{
    "Response": {
        "RequestId": "05c86278-f995-444b-b2b6-4798e3e3b67d"
    }
}
```

