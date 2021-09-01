**Example 1: 动态打包任务提交**



Input: 

```
tccli cdn CreateEdgePackTask --cli-unfold-argument  \
    --BlockID 0 \
    --CosBucket ‘edgepack-xxxxxxxx’ \
    --CosUriFrom ‘/apk/xxxx.apk’ \
    --CosUriTo ‘/out/xxxx.apk’
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

