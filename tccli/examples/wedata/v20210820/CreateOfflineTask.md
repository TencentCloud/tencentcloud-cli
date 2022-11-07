**Example 1: 创建离线任务**



Input: 

```
tccli wedata CreateOfflineTask --cli-unfold-argument  \
    --TypeId 0 \
    --ProjectId xx \
    --Notes xx \
    --TaskAction xx \
    --DelayTime 0 \
    --StartTime xx \
    --TaskName xx \
    --EndTime xx \
    --CycleStep 0 \
    --TaskMode xx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

