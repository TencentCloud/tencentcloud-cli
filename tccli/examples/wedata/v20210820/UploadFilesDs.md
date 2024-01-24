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
            "SecretId": "AKIDf31QcTcNY1Wv4lKpx5JWAfCKB0aeEXWOKe2L7RJHpZdVcPjq14iyHdgt35vGVKqx",
            "SecretKey": "12u32bi+f/Efo3xCBtxqIPQmI+GF8Na07o+Y25P2w1M=",
            "ShareStorageEndPoint": "service.cos.myqcloud.com",
            "ShareStorageType": "COS",
            "Token": "35A7Jdz9uwbijSzVBYYZKcgpOFn1yBDa6928bbdd4a9412f0e3a6f6cf8372a346G_cfFo-D8aDzgnLMh2krQH5B39nlTnrxD4-fqui_STmHnPQ9MaRtMVDbnXz5H_RmFZ6w_TFCe457YyyAFyHvSJusKkUZH8rGUBMi1ZBwZsUSHC6C5MVCJWtCx1xLMYy7x0CqUX3rkfPU1rNWQLHu431n7zdj7EpDeGtDFP1wttphJL0y5mwKQB_v50z1uF2KSTg9FhThqJKK8ityVlYpM6HZjaxKtyAAUJfyQHcgclaNjN0oN_wujl-R22kSdn8XWS0i4Q0Spe9Xqwb4QuxKYuoyn-cXwiULxu7O4saKC87cBZRUZzYtTZ18D1X9cNd5pMzquMDfYAL1rWBvPiJbtWDigitnzRiNPjJOtkRcjthaABj2w4WVW5C7SsEsvvV3XlpuDysolMNWte4xNbAvd3nLc-qSXng1fFaKSIhdNXAzuUCdnfy_3OQdnnIzBGnXFgO01fgjxTPlT8GAEt6wRZEu0JQDhvXWy3aUDU9_55vJTzoQSSPB5t4xNyY9AMVrWqjmTXMwijIbtC2En47B7EF_ijrJwIK7hXFfG3RHlIoq7jU2Y8zu7uhUP2y0OqD85PTLOVlCnZ0BFbX95E6-UO4-3_vfmoEFx1OoeEa_2FWWwWlLq2OiuedH6uTcwsFrf_FjpSd0QX-ZOQBxz3ZRoksj7x_SMEQLG5zu-Xh_5HmFchfA4Wy9aP2wn4hTpdRiwztm60Av9452HWWxIXbFn8_FhicOs3Y3DwMI1ZD504vM6q78IOeaH9_FbA58mk1-DHgtKp2RNiNIO_t9yZfjdYoyPqqsjDK8RytAbzk2TmepeNOIGJBoyB-ZJb8HE5_ph_ol2A9QNInrvdfwexWppCUqj6BWhOJwYM0kyQ8r9n90HdUAUJxp-mLqe8qd8wVQUoc350Ze_LEDYWyuhQLF85J-xK8w9sNjjon6sWp5rTt2XenLsFuzXgHgiUPYMjWKGyDc3EF3iCxsoZdgSG-SOdtPY1_rRLKddAVH_mVB91VM1hx6LSOESiPLO0eCt36j4kM3vF2L8DZnrhasMTfgPZ8nwBTFdAQkJqPIN0U4qWOlNxRGgukm8KGXYM73Qxwv-Fg0t3jd1VTRPHMV1duOwmnEqIGExACIobmHGSPPAxO-mhzbsIWHcKtfSsXrCl_S-z46pMvdeC9gCvq7EvDfHMzDyDGAve-ol5MgIDKrEQSYlougpwGKCTbqGozoqorztM1sfuAALerJJ7NmqrvHG_khISLDKvjX-POZ17oiMYAJtxNATMKJPGkj_y7J4q2WyMjoWS-AfQXckDr8MKmW2X7EEg4okhsZlbdUBCMVbZg3LYqqpwE1cBmjHY8too4RPfWrLNxXH5psud_TKgrsMKETfbbT-rj_gwCzFpjOrQm_BcUR4Zold0bfWKBn8us4O9QwTfe78Uazr3GcfyDyqxu_ejuqbeCe9t_Lltl_SF5ZtfiurnFfGqb8Q3muMufyQcz0IyDxubOHHAujhERzQdFH5RB50kScWVyBhT3Y5Hcd74nz-dTckKlVhQkthDaX2Rrs0Xeu5uyTv5_C4RAcWBYACjsUgOpXn2CnR22NzCR_Kvtpnpzcpp9LfieDmgAZjoXFme-HwkGfCgF1XR9FtA",
            "TokenCreateTime": 1687509957,
            "TokenExpiredTime": 1687517157
        },
        "RequestId": "51d424e8-8da8-4f32-9cf1-aca230d571f7"
    }
}
```

