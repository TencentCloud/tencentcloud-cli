**Example 1: 定义的物模型提交**



Input: 

```
tccli iotvideo CreateIotModel --cli-unfold-argument  \
    --ProductId 12345678910 \
    --IotModel {"properties":[{"id":"_productInfo","name":"产品信息","mode":"r","define":{"id":"_ProductInfo","name":"产品信息","type":[{"id":"productModel","name":"产品型号","type":"string32"},{"id":"productID","name":"产品ID","type":"string32"},{"id":"funcCode","name":"产品可选功能码","type":"uint32"},{"id":"revision","name":"物模型修订版本","type":"uint32"},{"id":"revisionUtc","name":"物模型修订时间","type":"uint32"}]}},{"id":"_versionInfo","name":"固件信息","mode":"r","define":{"id":"_VersionInfo","name":"固件信息","type":[{"id":"sdkVer","name":"SDK版本号","type":"uint32"},{"id":"swVer","name":"应用软件版本号","type":"uint32"},{"id":"hwVer","name":"硬件版本号","type":"uint32"}]}}],"actions":[]}
```

Output: 
```
{
    "Response": {
        "RequestId": "9187436e-0738-4449-ba8e-88882c59c9c9"
    }
}
```

