**Example 1: 获取cos 桶列表**



Input: 

```
tccli dlc ListTkeCosBuckets --cli-unfold-argument  \
    --BucketName aidanyxu-260209337 \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Buckets": [
            "aidanyxu-260209337"
        ],
        "RequestId": "31082488-5c57-45b8-a9f3-ac38a4dfa63a"
    }
}
```

