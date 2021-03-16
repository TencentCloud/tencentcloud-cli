**Example 1: 修改集群标签**

修改集群标签

Input: 

```
tccli tcaplusdb ModifyClusterTags --cli-unfold-argument  \
    --ReplaceTags.0.TagKey test1 \
    --ReplaceTags.0.TagValue value1 \
    --DeleteTags.0.TagKey delete1 \
    --DeleteTags.0.TagValue xx \
    --ClusterId 5674209986
```

Output: 
```
{
    "Response": {
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TaskId": "5674209986-1210"
    }
}
```

