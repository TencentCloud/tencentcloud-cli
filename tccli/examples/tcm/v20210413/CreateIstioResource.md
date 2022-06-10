**Example 1: CreateIstioResource**



Input: 

```
tccli tcm CreateIstioResource --cli-unfold-argument  \
    --MeshId xxxxx \
    --ResourcePath /apis/networking.istio.io/v1alpha3/namespaces/default/virtualservices \
    --Resource ...
```

Output: 
```
{
    "Response": {
        "RequestId": "request_id"
    }
}
```

