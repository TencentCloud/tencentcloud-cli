**Example 1: 获取固件上传路径**



Input: 

```
tccli iotvideo CreateUploadPath --cli-unfold-argument  \
    --ProductId 12345678910 \
    --FileName a.zip
```

Output: 
```
{
    "Response": {
        "Data": "https://ota-device-upgrade-1259781373.cos.ap-guangzhou.myqcloud.com/123456789000/a.zip?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDkY2928wGSrRhkx4FZ88IzIXZxSupxRis%26q-sign-time%3D1582081295%3B1582083095%26q-key-time%3D1582081295%3B1582083095%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D92a03e11de1ceb3b610597555e2a95bfe16dd05a",
        "RequestId": "0353288e-2fb9-4a85-b7fa-8519f21aee34"
    }
}
```

