**Example 1: 成功调用**

成功调用

Input: 

```
tccli ai3d SubmitTextureTo3DJob --cli-unfold-argument  \
    --File3D.Type GLB \
    --File3D.Url https://vcg-test-1258344699.cos.ap-guangzhou.myqcloud.com/test/3d/test.glb \
    --Prompt 优化模型
```

Output: 
```
{
    "Response": {
        "JobId": "1317417610996465664",
        "RequestId": "19f63401-d6f2-47d7-a3ad-8a3428a304ff"
    }
}
```

