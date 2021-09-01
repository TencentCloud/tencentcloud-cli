**Example 1: GetCrowdUploadInfo**



Input: 

```
tccli zj GetCrowdUploadInfo --cli-unfold-argument  \
    --FileName 111.txt \
    --License xsdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "ExpireTime": 1565768870,
            "SessionToken": "#######",
            "TmpSecretId": "########",
            "TmpSecretKey": "########",
            "CosInfo": {
                "Bucket": "zhuji-beta-1256886009",
                "Key": "/<FolderPath>/<FileName>.txt",
                "Region": "ap-shanghai"
            }
        },
        "RequestId": "123456789"
    }
}
```

