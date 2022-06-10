**Example 1: DeleteIstioResource**



Input: 

```
tccli tcm DeleteIstioResource --cli-unfold-argument  \
    --MeshId xxxxx \
    --ResourcePath /apis/networking.istio.io/v1alpha3/namespaces/default/virtualservices/test
```

Output: 
```
{
    "Response": {
        "RequestId": "request_id"
    }
}
```

