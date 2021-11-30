**Example 1: 操作TKE集群的addon**



Input: 

```
tccli tke ForwardApplicationRequestV3 --cli-unfold-argument  \
    --Method GET \
    --Path /api/v1/namespaces \
    --ClusterName cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ResponseBody": "[]",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

