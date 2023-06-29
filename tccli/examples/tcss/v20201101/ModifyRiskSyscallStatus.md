**Example 1: 修改高危系统调用事件状态**



Input: 

```
tccli tcss ModifyRiskSyscallStatus --cli-unfold-argument  \
    --EventIdSet 61c396cb85a03485f10c353e \
    --Status EVENT_INGNORE \
    --Remark 备注
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

