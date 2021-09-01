**Example 1: 创建表格组**

在集群下创建TcaplusDB表格组

Input: 

```
tccli tcaplusdb CreateTableGroup --cli-unfold-argument  \
    --TableGroupName tdr区1 \
    --ResourceTags.0.TagKey xx \
    --ResourceTags.0.TagValue xx \
    --ClusterId 6179109757 \
    --TableGroupId xx
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

