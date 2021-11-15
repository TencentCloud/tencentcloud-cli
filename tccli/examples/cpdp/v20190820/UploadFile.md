**Example 1: 身份证图片上传**



Input: 

```
tccli cpdp UploadFile --cli-unfold-argument  \
    --FileName demo.png \
    --FileType IdCard \
    --FileContent data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5QmCC
```

Output: 
```
{
    "Response": {
        "FileId": "file.png",
        "RequestId": "f64267a7-6a7d-4b0f-86de-b0e5fbae6847"
    }
}
```

**Example 2: 身份证图片上传加验证**



Input: 

```
tccli cpdp UploadFile --cli-unfold-argument  \
    --FileName demo.png \
    --FileType IdCardCheck \
    --FileExtendInfo.0.Type id_card_no \
    --FileExtendInfo.0.Value 110108200001011234 \
    --FileExtendInfo.1.Type id_card_name \
    --FileExtendInfo.1.Value 陈小小 \
    --FileContent data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5QmCC
```

Output: 
```
{
    "Response": {
        "FileId": "file.png",
        "RequestId": "f64267a7-6a7d-4b0f-86de-b0e5fbae6847"
    }
}
```

