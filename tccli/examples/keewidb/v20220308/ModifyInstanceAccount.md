**Example 1: 修改实例只读路由策略**



Input: 

```
tccli keewidb ModifyInstanceAccount --cli-unfold-argument  \
    --InstanceId kee-p04nodnb \
    --AccountName test-read-only \
    --Remark this is a read only account \
    --ReadonlyPolicy replication \
    --Privilege r \
    --AccountPassword Te******56
```

Output: 
```
{
    "Response": {
        "TaskId": 4294994446,
        "RequestId": "bd49e44c-7876-4880-bf9e-23be1709b94c"
    }
}
```

