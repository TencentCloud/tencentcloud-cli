**Example 1: Deleting table group**

This example shows you how to delete a table group based on cluster ID and table group ID.

Input: 

```
tccli tcaplusdb DeleteTableGroup --cli-unfold-argument  \
    --ClusterId 6179109757\
    --TableGroupId 1
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

