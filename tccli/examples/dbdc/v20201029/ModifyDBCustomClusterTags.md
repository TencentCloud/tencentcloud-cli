**Example 1: 为 DB Custom 集群修改标签**



Input: 

```
tccli dbdc ModifyDBCustomClusterTags --cli-unfold-argument  \
    --ClusterId dbcc-q428ovsf \
    --AddTags.0.Key Tag1 \
    --AddTags.0.Value Value1 \
    --DeleteTagKeys testKey
```

Output: 
```
{
    "Response": {
        "RequestId": "1ef4d109-8dd7-4ef1-9834-c652cd84bdf0"
    }
}
```

