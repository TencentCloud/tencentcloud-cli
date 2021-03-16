**Example 1: 删除表格组**

根据集群ID和表格组ID参数删除表格组

Input: 

```
tccli tcaplusdb DeleteTableGroup --cli-unfold-argument  \
    --TableGroupId 1 \
    --ClusterId 6179109757
```

Output: 
```
{
    "Response": {
        "RequestId": "1d7ba682-570c-4589-9624-7b463cd5d852",
        "TaskId": "6179109757-1208"
    }
}
```

