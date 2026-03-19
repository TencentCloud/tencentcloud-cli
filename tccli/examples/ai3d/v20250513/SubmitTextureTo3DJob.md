**Example 1: 调用示例**



Input: 

```
tccli ai3d SubmitTextureTo3DJob --cli-unfold-argument  \
    --File3D.Type GLB \
    --File3D.Url https://cos.ap-guangzhou.myqcloud.com/xxx.glb \
    --Prompt 优化模型
```

Output: 
```
{
    "Response": {
        "JobId": "1425050619077222400",
        "RequestId": "dcc06f5c-684d-4e58-9eaf-2616d66b177a"
    }
}
```

