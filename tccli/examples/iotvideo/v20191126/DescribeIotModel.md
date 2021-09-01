**Example 1: 查询物模型定义**



Input: 

```
tccli iotvideo DescribeIotModel --cli-unfold-argument  \
    --ProductId 12345678910 \
    --Revision 1
```

Output: 
```
{
    "Response": {
        "RequestId": "2444e6d7-1e3b-4a0e-9be5-202c4afdd228",
        "Data": "{\"properties\":[{\"id\":\"_productInfo\",\"name\":\"产品信息\",\"mode\":\"r\",\"define\":{\"id\":\"_ProductInfo\",\"name\":\"产品信息\",\"type\":[{\"name\":\"产品型号\",\"id\":\"productModel\",\"type\":\"string32\"},{\"name\":\"产品ID\",\"id\":\"productID\",\"type\":\"string32\"},{\"name\":\"产品可选功能码\",\"id\":\"funcCode\",\"type\":\"uint32\"},{\"name\":\"物模型修订版本\",\"id\":\"revision\",\"type\":\"uint32\"},{\"name\":\"物模型修订时间\",\"id\":\"revisionUtc\",\"type\":\"uint32\"}]}},{\"id\":\"_versionInfo\",\"name\":\"固件信息\",\"mode\":\"r\",\"define\":{\"id\":\"_VersionInfo\",\"name\":\"固件信息\",\"type\":[{\"name\":\"SDK版本号\",\"id\":\"sdkVer\",\"type\":\"uint32\"},{\"name\":\"应用软件版本号\",\"id\":\"swVer\",\"type\":\"uint32\"},{\"name\":\"硬件版本号\",\"id\":\"hwVer\",\"type\":\"uint32\"}]}},{\"id\":\"_otaMode\",\"name\":\"OTA升级模式(内置对象)\",\"mode\":\"rw\",\"define\":{\"type\":\"int32\"}},{\"id\":\"_logLevel\",\"name\":\"日志输出等级设置(内置对象)\",\"mode\":\"rw\",\"define\":{\"type\":\"int32\"}},{\"id\":\"_cloudStoage\",\"name\":\"云存储服务参数(内置对象)\",\"mode\":\"rw\",\"define\":{\"id\":\"_CloudStorageService\",\"name\":\"云存储服务参数\",\"type\":[{\"name\":\"云存储服务类型\",\"id\":\"serviceType\",\"type\":\"int32\"},{\"name\":\"云存储服务过期时间(UTC)\",\"id\":\"utcExpire\",\"type\":\"int32\"},{\"name\":\"云存储服务暂停,设置为非0时,即使当前存在有效的云存储套餐,设备也不会云存推流\",\"id\":\"pause\",\"type\":\"int32\"},{\"name\":\"云存储服务参数信息\",\"id\":\"serviceParm\",\"type\":\"string128\"}]}}],\"actions\":[{\"id\":\"_otaVersion\",\"name\":\"OTA升级版本(内置对象)\",\"type\":\"string32\"},{\"id\":\"_otaUpgrade\",\"name\":\"OTA升级进度(内置对象)\",\"type\":\"int32\"}]}"
    }
}
```

