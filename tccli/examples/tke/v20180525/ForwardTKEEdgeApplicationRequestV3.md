**Example 1: 操作TKE集群的addon**



Input: 

```
tccli tke ForwardTKEEdgeApplicationRequestV3 --cli-unfold-argument  \
    --Method GET \
    --Path /apis/application.tkestack.io/v1/namespaces/cls-xxxx/apps \
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

