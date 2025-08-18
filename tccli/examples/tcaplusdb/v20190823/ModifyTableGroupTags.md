**Example 1: 修改表格组标签**

修改表格组标签

Input: 

```
tccli tcaplusdb ModifyTableGroupTags --cli-unfold-argument  \
    --ClusterId 5674209986 \
    --TableGroupId 1 \
    --ReplaceTags.0.TagKey test1 \
    --ReplaceTags.0.TagValue value1 \
    --DeleteTags.0.TagKey delete1
```

Output: 
```
{
    "Response": {
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TaskId": "5674209986-1211"
    }
}
```

