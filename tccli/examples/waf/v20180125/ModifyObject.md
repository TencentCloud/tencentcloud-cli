**Example 1: 修改防护对象**



Input: 

```
tccli waf ModifyObject --cli-unfold-argument  \
    --ObjectId lb-vsf13vzg \
    --Status 0 \
    --InstanceId waf_vxj234vxcfnm \
    --OpType Status \
    --Proxy 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

