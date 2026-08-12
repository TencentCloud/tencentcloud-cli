**Example 1: 修改 DB Custom 集群属性**

开启集群删除保护

Input: 

```
tccli dbdc ModifyDBCustomClusterAttributes --cli-unfold-argument  \
    --ClusterId dbcc-hq867qji \
    --DeletionProtection True
```

Output: 
```
{
    "Response": {
        "RequestId": "6ba3094b-eea5-4f62-ac2f-97b44f251944"
    }
}
```

