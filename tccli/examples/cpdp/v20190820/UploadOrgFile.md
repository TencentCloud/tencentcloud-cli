**Example 1: 上传机构文件接口成功示例**

上传机构文件接口成功

Input: 

```
tccli cpdp UploadOrgFile --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --FileContent iVBORw0KGgoAAAANSUhEUgAAAI8AAAAeCAYAAAAVWU11AAAACXBIWXMAAAsTAAAL \
    --FileMd5 E68A2FEBA43406F3D27B38F71E1C39A7 \
    --FileExtension jpg \
    --Storage 1
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "提交成功",
        "Result": {
            "Storage": "1",
            "FilePath": "201912/eabc9ba6b7a5d577011def3a9f4c5302.png"
        }
    }
}
```

