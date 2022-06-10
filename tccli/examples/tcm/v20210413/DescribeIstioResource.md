**Example 1: DescribeIstioResource**



Input: 

```
tccli tcm DescribeIstioResource --cli-unfold-argument  \
    --MeshId xxxxxx \
    --ResourcePath /apis/networking.istio.io/v1alpha3/namespaces//serviceentries
```

Output: 
```
{
    "Response": {
        "RequestId": "request_id",
        "Resource": "{\"apiVersion\":\"networking.istio.io/v1alpha3\",\"items\":[],\"kind\":\"ServiceEntryList\",\"metadata\":{\"continue\":\"\",\"resourceVersion\":\"3737767636\",\"selfLink\":\"/apis/networking.istio.io/v1alpha3/namespaces//serviceentries\"}}\n"
    }
}
```

