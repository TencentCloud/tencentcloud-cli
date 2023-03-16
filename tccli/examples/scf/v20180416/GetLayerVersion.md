**Example 1: 获取层版本详情**

获取层版本详情

Input: 

```
tccli scf GetLayerVersion --cli-unfold-argument  \
    --LayerName abc \
    --LayerVersion 0
```

Output: 
```
{
    "Response": {
        "Status": "Active",
        "LayerVersion": 1,
        "CodeSha256": "c7c8bda601817ce4faab4c4fb3e73b9a32040e0e9f31f7a649d84d4bdde9e4a5",
        "Description": "desc",
        "LicenseInfo": "",
        "AddTime": "2019-11-26 16:15:33",
        "Location": "https://lambdalayerin-1253665819.cos.ap-mumbai.myqcloud.com/1253970226/layer3/1/1253970226_layer3_1.zip?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDqbBtfGe4eSSK8CExGjmC0e8Qcnswv6yj%26q-sign-time%3D1582083327%3B1582093387%26q-key-time%3D1582083327%3B1582093387%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D255d3e5aaa6c7224396b39f857e134a0dfb27c89&response-content-type=application/octet-stream",
        "CompatibleRuntimes": [
            "Nodejs8.9",
            "Nodejs6.10"
        ],
        "LayerName": "layer3",
        "RequestId": "6c7578ed-b816-4e50-930a-54e855452b8b"
    }
}
```

