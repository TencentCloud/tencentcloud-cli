**Example 1: 推送节点数据（value支持数值字符串）**



Input: 

```
tccli tan CreateBlockNodeRecords --cli-unfold-argument  \
    --Records [{"key1":123,"key2":"string"}] \
    --GroupId tan-xxxx \
    --NodeId b5fd85a5-033a-4f28-ab87-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: 推送节点数据（支持多条数据推送，最大不超过100条）**



Input: 

```
tccli tan CreateBlockNodeRecords --cli-unfold-argument  \
    --Records [{"key1":1,"key2":"value2"},{"key1":2,"key2":"value2"}] \
    --GroupId tan-xxxx \
    --NodeId b5fd85a5-033a-4f28-ab87-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

