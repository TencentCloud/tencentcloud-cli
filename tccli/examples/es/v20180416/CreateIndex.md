**Example 1: 创建自治索引**

创建自治索引

Input: 

```
tccli es CreateIndex --cli-unfold-argument  \
    --Username elastic \
    --IndexName test \
    --IndexType normal \
    --InstanceId es-abcdefgh \
    --IndexMetaJson {} \
    --Password 123456
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

