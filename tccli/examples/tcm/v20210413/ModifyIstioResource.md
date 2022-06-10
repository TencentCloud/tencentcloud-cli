**Example 1: ModifyIstioResource**



Input: 

```
tccli tcm ModifyIstioResource --cli-unfold-argument  \
    --MeshId xxxxxx \
    --ResourcePath /apis/networking.istio.io/v1alpha3/namespaces/default/virtualservices/test \
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

