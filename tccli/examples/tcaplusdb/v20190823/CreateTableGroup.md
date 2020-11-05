**Example 1: Creating table group**

This example shows you how to create a TcaplusDB table group in a cluster.

Input: 

```
tccli tcaplusdb CreateTableGroup --cli-unfold-argument  \
    --ClusterId 6179109757\
    --TableGroupName 'tdr zone 1'
```

Output: 
```
{
    "Response": {
        "TableGroupId": "1",
        "RequestId": "d87c0378-47af-4d59-920d-82fd2a778e6c"
    }
}
```

