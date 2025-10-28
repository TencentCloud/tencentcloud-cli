**Example 1: 修改固件升级任务状态为取消状态**

当固件任务在升级过程需要取消时可使用。或修改为其它允许的状态



Input: 

```
tccli iotexplorer UpdateOtaTaskStatus --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TaskId 11001 \
    --Status 6
```

Output: 
```
{
    "Response": {
        "RequestId": "sjalifekj-dsakfjleija-3dskjf-sdaklfj"
    }
}
```

