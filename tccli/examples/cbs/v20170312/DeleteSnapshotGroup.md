**Example 1: 删除快照组**

删除快照组，并同时删除快照组绑定的镜像。

Input: 

```
tccli cbs DeleteSnapshotGroup --cli-unfold-argument  \
    --SnapshotGroupId csnap-gv9naz6b \
    --DeleteBindImages true
```

Output: 
```
{
    "Response": {
        "RequestId": "d7c2dd0f-59b1-4243-af5f-8443a1527daa"
    }
}
```

