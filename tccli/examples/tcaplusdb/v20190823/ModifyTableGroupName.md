**Example 1: Renaming table group**

This example shows you how to rename a table group.

Input: 

```
tccli tcaplusdb ModifyTableGroupName --cli-unfold-argument  \
    --ClusterId 6179109757\
    --TableGroupId 1\
    --TableGroupName 'tdr test zone 1'
```

Output: 
```
{
    "Response": {
        "RequestId": "c3d85d90-65a6-46ed-9187-b2a429e18cfc"
    }
}
```

