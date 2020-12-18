**Example 1: 修改资源标签列表**

修改资源标签列表

Input: 

```
tccli chdfs ModifyResourceTags --cli-unfold-argument  \
    --FileSystemId f1mhaqkciq0 \
    --Tags.0.Key key1 \
    --Tags.0.Value value1 \
    --Tags.1.Key key2 \
    --Tags.1.Value value2
```

Output: 
```
{
    "Response": {
        "RequestId": "61046a25-2eda-4495-b9b6-eab6edf41d79"
    }
}
```

