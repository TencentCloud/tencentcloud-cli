**Example 1: 移除复制组中的实例**

移除复制组的实例，数据同步类型为强同步。

Input: 

```
tccli redis RemoveReplicationInstance --cli-unfold-argument  \
    --InstanceId crs-sa5**** \
    --SyncType True \
    --GroupId crs-rpl-sa5****
```

Output: 
```
{
    "Response": {
        "RequestId": "c4ed5948-d156-4931-b9c3-10133a0bb6c9",
        "TaskId": 10856
    }
}
```

