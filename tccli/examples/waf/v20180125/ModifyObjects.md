**Example 1: 批量绑定实例ID**



Input: 

```
tccli waf ModifyObjects --cli-unfold-argument  \
    --ObjectId lb-acvfds \
    --OpType InstanceId \
    --InstanceId waf_000000111
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

