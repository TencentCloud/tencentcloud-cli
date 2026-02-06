**Example 1: 暂停或者取消集群更新参数任务**



Input: 

```
tccli tke ModifyClusterExtraArgsTaskState --cli-unfold-argument  \
    --ClusterId cls-da481xax \
    --Operation abort
```

Output: 
```
{
    "Response": {
        "RequestId": "8ec3f44c-3460-4c61-89e4-fe97f14c3fc7"
    }
}
```

