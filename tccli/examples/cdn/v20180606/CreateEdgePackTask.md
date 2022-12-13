**Example 1: 动态打包任务提交**



Input: 

```
tccli cdn CreateEdgePackTask --cli-unfold-argument  \
    --CosBucket ‘edgepack-bucket1’ \
    --BlockID 0 \
    --CosUriTo ‘/out/app_out.apk’ \
    --CosUriFrom ‘/apk/app.apk’
```

Output: 
```
{
    "Response": {
        "RequestId": "19d1096d-a4e8-4607-bfca-840a3f515378"
    }
}
```

