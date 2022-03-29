**Example 1: 获取机构账单文件下载地址成功示例**



Input: 

```
tccli cpdp GetBillDownloadUrl --cli-unfold-argument  \
    --OpenId OpenId123 \
    --OpenKey OpenKey123 \
    --Day 20220322
```

Output: 
```
{
    "Response": {
        "RequestId": "3402a086-bd77-4ee9-bc9a-4cf0c87b6c64",
        "ErrCode": "0",
        "ErrMessage": "成功",
        "Result": {
            "DownloadUrl": "https://tencent.com/Fileup1/orderexport/download?key=123"
        }
    }
}
```

