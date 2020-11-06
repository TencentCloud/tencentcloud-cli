**Example 1: 获取设备物模型**



Input: 

```
tccli iotvideo DescribeDeviceModel --cli-unfold-argument  \
    --Tid ******** \
    --Branch ****
```

Output: 
```
{
    "Response": {
        "RequestId": "fcf53f95-9887-4f26-b0cf-2df2c463b06d",
        "Data": {
            "Tid": "xxxx",
            "Branch": "",
            "IotModel": "{\"Action\":{\"_otaVersion\":{\"ctlVal\":\"\",\"origin\":\"\",\"t\":0},\"_otaUpgrade\":{\"ctlVal\":0,\"origin\":\"\",\"t\":0},\"cameraOn\":{\"ctlVal\":0,\"origin\":\"\",\"t\":0},\"takePhoto\":{\"ctlVal\":0,\"origin\":\"\",\"t\":0},\"shootVideo\":{\"ctlVal\":0,\"origin\":\"\",\"t\":0},\"presetPosition\":{\"ctlVal\":0,\"origin\":\"\",\"t\":0}},\"ProConst\":{\"_productInfo\":{\"productModel\":\"\",\"productID\":\"12345\",\"funcCode\":1,\"revision\":1,\"revisionUtc\":1},\"_versionInfo\":{\"sdkVer\":0,\"swVer\":2019,\"hwVer\":2019}},\"ProWritable\":{\"_otaMode\":{\"setVal\":0,\"t\":0},\"_logLevel\":{\"setVal\":2,\"t\":1581993565},\"_cloudStoage\":{\"setVal\":{\"serviceType\":0,\"utcExpire\":0,\"pause\":0,\"serviceParm\":\"\"},\"t\":0},\"recodePlan\":{\"setVal\":{\"timeSection1\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection2\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection3\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection4\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection5\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection6\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection7\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0},\"timeSection8\":{\"desc\":\"\",\"enable\":0,\"dayOfWeek\":0,\"begin\":0,\"end\":0}},\"t\":0},\"presetPosSetting\":{\"setVal\":{\"pos1\":{\"x\":101,\"y\":13},\"pos2\":{\"x\":100,\"y\":200},\"pos3\":{\"x\":10,\"y\":0},\"pos4\":{\"x\":122,\"y\":123},\"pos5\":{\"x\":0,\"y\":0},\"pos6\":{\"x\":0,\"y\":0}},\"t\":1582168513}},\"ProReadonly\":{\"_online\":{\"stVal\":1,\"t\":1581926411},\"_otaVersion\":{\"stVal\":\"\",\"t\":0},\"_otaUpgrade\":{\"stVal\":0,\"t\":0},\"cameraOn\":{\"stVal\":0,\"t\":0},\"takePhoto\":{\"stVal\":0,\"t\":0},\"shootVideo\":{\"stVal\":0,\"t\":0},\"presetPosition\":{\"stVal\":0,\"t\":0},\"test\":{\"stVal\":{\"attr1\":0,\"attr2\":\"\",\"attr3\":{\"attr3_1\":0,\"attr3_2\":0},\"attr4\":{\"attr4_1\":0,\"attr4_2\":\"\",\"attr4_3\":{\"attr4_3_1\":0,\"attr4_3_2\":0}}},\"t\":0}}}"
        }
    }
}
```

