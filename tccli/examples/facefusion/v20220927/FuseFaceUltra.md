**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli facefusion FuseFaceUltra --cli-unfold-argument  \
    --ModelUrl https://cos.ap-guangzhou.myqcloud.com/facefusion/FuseFaceUltra/model.png \
    --RspImgType base64 \
    --MergeInfos.0.Url https://cos.ap-guangzhou.myqcloud.com/facefusion/FuseFaceUltra/input.png \
    --FusionUltraParam.WarpRadio 1.2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.ParameterValueError",
            "Message": "FusionParam值不合法。"
        },
        "RequestId": "89cdd6c5-cb8f-4cbe-959b-e249f3753f55"
    }
}
```

**Example 2: 调用成功示例**

调用成功示例

Input: 

```
tccli facefusion FuseFaceUltra --cli-unfold-argument  \
    --ModelUrl https://cos.ap-guangzhou.myqcloud.com/facefusion/FuseFaceUltra/model.png \
    --RspImgType url \
    --MergeInfos.0.Url https://cos.ap-guangzhou.myqcloud.com/facefusion/FuseFaceUltra/input.png \
    --FusionUltraParam.WarpRadio 0.7
```

Output: 
```
{
    "Response": {
        "FusedImage": "https://cos.ap-guangzhou.myqcloud.com/facefusion/FuseFaceUltra/output.png",
        "RequestId": "06f9b251-fa48-435e-b391-145d67919b2c"
    }
}
```

