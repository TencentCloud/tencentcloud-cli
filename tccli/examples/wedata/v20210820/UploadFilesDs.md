**Example 1: 示例1**

demo_3.csv 文件已经存在，生成了新的文件名，上传时使用新的文件名

Input: 

```
tccli wedata UploadFilesDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --FileNames demo_3.csv demo_4.csv demo_5.csv \
    --OriginDomain 
```

Output: 
```
{
    "Response": {
        "Data": {
            "BucketName": "wedata-fusion-dev-1257305158",
            "BucketRegion": "ap-nanjing",
            "FileExpireTime": -1,
            "FileMappings": [
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/import/1460947878944567296/demo_5.csv",
                    "OriginFileName": "demo_5.csv",
                    "TargetFileName": "demo_5.csv"
                },
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/import/1460947878944567296/demo_4.csv",
                    "OriginFileName": "demo_4.csv",
                    "TargetFileName": "demo_4.csv"
                },
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/import/1460947878944567296/demo_3_269989484935.csv",
                    "OriginFileName": "demo_3.csv",
                    "TargetFileName": "demo_3_269989484935.csv"
                }
            ],
            "SecretId": "AKIDf31QcTcNY1Wv4lKpx567890",
            "SecretKey": "12u32bi+f/Efo3xCBtxqIPQ7890",
            "ShareStorageEndPoint": "service.cos.myqcloud.com",
            "ShareStorageType": "COS",
            "Token": "35A7Jdz9uwbijSzVBYYZKcgpOFn1yBDa6928bbdd4a9412f0e3a6f6cf8372a346G_cfFo-D8aDzgnLMh2krQH5B39nlTnrxD4",
            "TokenCreateTime": 1687509957,
            "TokenExpiredTime": 1687517157
        },
        "RequestId": "51d424e8-8da8-4f32-9cf1-aca230d571f7"
    }
}
```

