**Example 1: Renaming cluster**

This example shows you how to rename a cluster based on ClusterId.

Input: 

```
tccli tcaplusdb ModifyClusterName --cli-unfold-argument  \
    --ClusterId 5674209986\
    --ClusterName 'gz test PROTO'
```

Output: 
```
{
    "Response": {
        "RequestId": "87562838-1eda-45f3-abda-59a704135fe7"
    }
}
```

