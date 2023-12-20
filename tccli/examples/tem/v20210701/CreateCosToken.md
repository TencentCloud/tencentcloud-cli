**Example 1: 生成Cos临时密钥**

为上传jar包和war包，生成Cos临时密钥

Input: 

```
tccli tem CreateCosToken --cli-unfold-argument  \
    --PkgName test.jar \
    --TimeVersion 1.0 \
    --ApplicationId app-testid \
    --SourceChannel 0 \
    --OptType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": {}
    }
}
```

