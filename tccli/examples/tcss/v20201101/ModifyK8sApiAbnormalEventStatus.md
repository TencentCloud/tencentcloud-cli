**Example 1: 修改k8sapi异常事件状态**



Input: 

```
tccli tcss ModifyK8sApiAbnormalEventStatus --cli-unfold-argument  \
    --Status xx \
    --Remark xx \
    --EventIDSet 1
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd"
    }
}
```

