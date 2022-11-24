**Example 1: 修改AccessLog配置**



Input: 

```
tccli tcm ModifyAccessLogConfig --cli-unfold-argument  \
    --EnableStdout true \
    --Template "istio" \
    --MeshId "mesh-xxx"
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

