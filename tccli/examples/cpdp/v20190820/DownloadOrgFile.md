**Example 1: 下载文件接口成功示例**

下载文件接口成功

Input: 

```
tccli cpdp DownloadOrgFile --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec \
    --FilePath 201912/eabc9ba6b7a5d577011def3a9f4c5302.png \
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
            "Content": "iVBORw0KGgoAAAANSUhEUgAAAI8AAAAeCAYAAAAVWU11AAAACXBIWXMAAAsTAAAL"
        }
    }
}
```

