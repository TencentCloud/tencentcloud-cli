**Example 1: 成功结果**



Input: 

```
tccli faceid GetWebVerificationResult --cli-unfold-argument  \
    --BizToken EE13636D-1985-42CA-BD61-73F4C8B687E6
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "ErrorMsg": "Success",
        "RequestId": "a6e62364-60d4-4eb6-8908-da3ff3d601f8",
        "VerificationDetailList": [
            {
                "ErrorCode": 0,
                "ErrorMsg": "Success",
                "LivenessErrorCode": 0,
                "LivenessErrorMsg": "Success",
                "CompareErrorCode": 0,
                "CompareErrorMsg": "Success",
                "Similarity": 100,
                "ReqTimestamp": 1637291599353,
                "Seq": "7269e30e-c142-46ba-aa60-b5677bf69d24"
            }
        ],
        "VideoBestFrameMd5": "30fa34052530d0ba033b956d06eb89b5",
        "VideoBestFrameUrl": "https://xxx.cos.ap-singapore.myqcloud.com/faceid.png?q-sign-algorithm=sha1&q-ak=AKIDRPHPMw6HL4PeDO175x_vY2hjAja5nFelfAiy60n0irDQLQWYSZ0dfJ1tIrTjFOSJ&q-sign-time=1637637685;1637641285&q-key-time=1637637685;1637641285&q-header-list=host&q-url-param-list=&q-signature=bab269f6585d3f42a60d0ad4e94e229e6d3f8959&x-cos-security-token=ZR3Vx8aT4Dgb5c95F7FIMc9Pw6hC25baea5274fa45568cd34ca7c53a3867ec4aB5vbfkJ5tM3Td3p18cMurjkx1YsMN0WeEQFzoSTDpi9z0Y4UYktcEk6ewfErVQmuyX2za_xh0a1KhvWf7et0d0XHl4nHXhPTjzgUVazrdIRFhcfO0VKO12T2MoN-cN_Ltp5jasLW7PUTVRZFDvkXCxVSsvxb15W1gdX_7K8x2fORKSMjbQqAL51EB19SD4R2",
        "VideoMd5": "30fa34052530d0ba033b956d06eb89b5",
        "VideoUrl": "https://xxx.cos.ap-singapore.myqcloud.com/faceid.png?q-sign-algorithm=sha1&q-ak=AKIDRPHPMw6HL4PeDO175x_vY2hjAja5nFelfAiy60n0irDQLQWYSZ0dfJ1tIrTjFOSJ&q-sign-time=1637637685;1637641285&q-key-time=1637637685;1637641285&q-header-list=host&q-url-param-list=&q-signature=bab269f6585d3f42a60d0ad4e94e229e6d3f8959&x-cos-security-token=ZR3Vx8aT4Dgb5c95F7FIMc9Pw6hC25baea5274fa45568cd34ca7c53a3867ec4aB5vbfkJ5tM3Td3p18cMurjkx1YsMN0WeEQFzoSTDpi9z0Y4UYktcEk6ewfErVQmuyX2za_xh0a1KhvWf7et0d0XHl4nHXhPTjzgUVazrdIRFhcfO0VKO12T2MoN-cN_Ltp5jasLW7PUTVRZFDvkXCxVSsvxb15W1gdX_7K8x2fORKSMjbQqAL51EB19SD4R2"
    }
}
```

