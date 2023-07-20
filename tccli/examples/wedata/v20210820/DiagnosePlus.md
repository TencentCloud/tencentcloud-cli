**Example 1: test**

test

Input: 

```
tccli wedata DiagnosePlus --cli-unfold-argument  \
    --SearchCondition.Instance.TaskId 20230101114142907 \
    --SearchCondition.Instance.CurRunDate 2023-03-15 15:00:00 \
    --ProjectId 1460947878944567296
```

Output: 
```
{
    "Response": {
        "Data": "诊断信息：\n该实例被手动终止\n可能原因：\n由用户在实例运维执行\"终止\"操作\n操作指引：\n无",
        "RequestId": "46e2f9ef-28de-448c-bd41-cf3d4db4727c"
    }
}
```

