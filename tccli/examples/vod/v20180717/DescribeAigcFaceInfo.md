**Example 1: 获取人脸信息**



Input: 

```
tccli vod DescribeAigcFaceInfo --cli-unfold-argument  \
    --SubAppId 251007502 \
    --FileInfos.0.Type Url \
    --FileInfos.0.Url https://150*************myqcloud.com/a288b1b2vodtran*************/ee8d47************700322201/v.f100020.mp4
```

Output: 
```
{
    "Response": {
        "FaceInfoSet": [
            {
                "FaceInfoList": [
                    {
                        "EndTime": 8300,
                        "FaceId": "0",
                        "FaceImage": "https://p4-***********.com/ksc2/PwuLBM-5dzj_j1G7Rknhv_y0AJnN3Dbcc_OLXsEBfQbx7bGOUdOVBuJ5wKif7oKOSiGyDYi2lVSohyo-lUOJfNI-9BloWg0hz-hQ4Kprbl8.jpg?cacheKey=ChtzZWN1cml0eS5rbGluZy5tZXRhX2VuY3J5cHQSYIQuk1zV3s4miMifxDwaHLonhr-U2j-wtS1-Rh1DG9rNFOY184QrnGDu-OtDbWejcQcX6C_j8ymp3g8vCLmZitMpyyA9ayaYeYVuPWEKG_hTFaby9KV9xh7o-Dw_yzSrhhoSI394zzPJZ_uhWSjkByU4CYy1IiAmL-aebPeMm7WkoDpRUJQS1q1nmIauc4OI_7ly72QRXygFMAE&x-kcdn-pid=112757&pkey=AAUchViCWGXo5LLMOiMgoZSHnS5dHjJ529n4C4o-4lHRPI9ArlFppz7ON5xvp1NZKaciNO0puXbdtPUqq3Y1Lryw55fANTDmMO8vkVcxGKevc-Ros3qJD1rGJlarXjnqkks",
                        "StartTime": 0
                    }
                ],
                "SessionId": "845692****60512089"
            }
        ],
        "RequestId": "509ed24c-7a76-4328-98b2-a8e2428dd858"
    }
}
```

