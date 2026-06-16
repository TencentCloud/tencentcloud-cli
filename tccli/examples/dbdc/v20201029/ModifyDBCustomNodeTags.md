**Example 1: 为 DB Custom 节点修改标签**



Input: 

```
tccli dbdc ModifyDBCustomNodeTags --cli-unfold-argument  \
    --NodeId dbcn-j4xd1241 \
    --AddTags.0.Key 测试标签Key \
    --AddTags.0.Value 测试标签Value \
    --DeleteTagKeys testkey
```

Output: 
```
{
    "Response": {
        "RequestId": "a4c6c23f-62bb-4568-a107-141c65290f8c"
    }
}
```

