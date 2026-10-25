**Example 1: 示例**



Input: 

```
tccli rum UploadMiniProgramSource --cli-unfold-argument  \
    --AppId 1****7 \
    --Release 1.0.0 \
    --FileBase64 UEsDBAoAAAAAA \
    --FileName mp-source.zip
```

Output: 
```
{
    "Response": {
        "Result": "{\"PackId\":\"mpr_1\",\"AppId\":\"1****7\",\"BundleHash\":\"a1b2c3d4e5f67890\",\"Status\":\"ready\",\"Idempotent\":false}",
        "ErrorMsg": "",
        "RequestId": "c3ede0ff-9a91-4312-ac09-b2d8f7c597c7"
    }
}
```

