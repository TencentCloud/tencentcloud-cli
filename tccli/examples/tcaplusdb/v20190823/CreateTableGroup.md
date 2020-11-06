**Example 1: 创建表格组**

在集群下创建TcaplusDB表格组

Input: 

```
tccli tcaplusdb CreateTableGroup --cli-unfold-argument  \
    --ClusterId 6179109757 \
    --TableGroupName tdr区1
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

