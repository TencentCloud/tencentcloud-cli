**Example 1: 获取创建法人章二维码成功**

获取创建法人章二维码

Input: 

```
tccli ess CreateLegalSealQrCode --cli-unfold-argument  \
    --Operator.UserId yDwfsUUckpsqt647UE6uSrk1ZWhYH56z
```

Output: 
```
{
    "Response": {
        "QrcodeBase64": "5X8Af8AwfOf84uv+72f/fR6APgD/gyp/wCUpvx8/wCzAPin/wCtFfsq1/oOf8FNvCfirx7/AME2/wDgoN4F8C+GfEHjTxt40/Yg/av8J+DvB3hPRtR8R+KvFnirxH8BvH2j+HvDPhnw9o9teavr3iDXd（其他图片BASE64编码省略）",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

