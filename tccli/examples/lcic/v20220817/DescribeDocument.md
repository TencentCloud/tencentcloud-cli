**Example 1: 测试示例**

pdf 示例

Input: 

```
tccli lcic DescribeDocument --cli-unfold-argument  \
    --DocumentId omxxxsdc
```

Output: 
```
{
    "Response": {
        "DocumentId": "omxxxsdc",
        "DocumentName": "滴滴电子发票 (1).pdf",
        "DocumentSize": 38673,
        "DocumentType": "pdf",
        "DocumentUrl": "https://tcic-source.qcloudclass.com/uploads/5390248a-5eb7-4fe8-be27-c43dbad1380f/3520371/1679021408_KzpMGD38.pdf",
        "Owner": "2N1zP0mW7E3Vr3xJ2ZQ9GeFDK4t",
        "Pages": 1,
        "Permission": 0,
        "RequestId": "ee3fdca0-c88c-43f1-81b4-4f51f9e50521",
        "SdkAppId": 3520371,
        "TranscodeInfo": "",
        "TranscodeProgress": 100,
        "TranscodeResult": "https://tcic-test-1257307760.qcloudclass.com/doc/01aq2v7djsh31noat9gc_tiw/picture/",
        "TranscodeState": 3,
        "TranscodeType": 1,
        "UpdateTime": 1679021410
    }
}
```

**Example 2: 获取文档详情**

示例

Input: 

```
tccli lcic DescribeDocument --cli-unfold-argument  \
    --DocumentId ntxsfrzk
```

Output: 
```
{
    "Response": {
        "DocumentId": "ntxsfrzk",
        "DocumentName": "test.pptx",
        "DocumentSize": 15814364,
        "DocumentType": "pptx",
        "DocumentUrl": "https://tcic-source.qcloudclass.com/uploads/5390248a-5eb7-4fe8-be27-c43dbad1380f/3520371/1677202414_85bt9f0X.pptx",
        "Owner": "2M04q0j5mhsbq1lAEbCW1dhRvA2",
        "Pages": 0,
        "Permission": 0,
        "RequestId": "d97f98d7-de89-455a-a1f3-b9dae84d84bb",
        "SdkAppId": 3520371,
        "TranscodeInfo": "Microsoft Macintosh PowerPoint",
        "TranscodeProgress": 100,
        "TranscodeResult": "https://tcic-test-1257307760.qcloudclass.com/doc/gsutgbm7ssh31ns71sfc_tiw/h5/index.html",
        "TranscodeState": 3,
        "TranscodeType": 1,
        "UpdateTime": 1677202419
    }
}
```

**Example 3: 示例**

课件预览示例

Input: 

```
tccli lcic DescribeDocument --cli-unfold-argument  \
    --DocumentId ntxsfrzk
```

Output: 
```
{
    "Response": {
        "DocumentId": "ntxsfrzk",
        "DocumentName": "test.pptx",
        "DocumentSize": 15814364,
        "DocumentType": "pptx",
        "DocumentUrl": "https://tcic-source.qcloudclass.com/uploads/5390248a-5eb7-4fe8-be27-c43dbad1380f/3520371/1677202414_85bt9f0X.pptx",
        "Owner": "2M04q0j5mhsbq1lAEbCW1dhRvA2",
        "Pages": 2,
        "Permission": 0,
        "Preview": "https://class.qcloudclass.com/temp/preview.html?isppt=1&url=https://tcic-test-1257307760.qcloudclass.com/doc/gsutgbm7ssh31ns71sfc_tiw/h5/index.html&total=2",
        "RequestId": "8a7bafba-bc67-4040-8203-475532db535f",
        "SdkAppId": 3520371,
        "TranscodeInfo": "Microsoft Macintosh PowerPoint",
        "TranscodeProgress": 100,
        "TranscodeResult": "https://tcic-test-1257307760.qcloudclass.com/doc/gsutgbm7ssh31ns71sfc_tiw/h5/index.html",
        "TranscodeState": 3,
        "TranscodeType": 1,
        "UpdateTime": 1677202419
    }
}
```

