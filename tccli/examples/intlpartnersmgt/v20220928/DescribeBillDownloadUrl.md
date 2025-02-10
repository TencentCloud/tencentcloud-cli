**Example 1: DescribeBillDownloadUrl-1**

子客获取自己的账单链接。请求下载文件生成中，请等待文件生成完成后重新下载

Input: 

```
tccli intlpartnersmgt DescribeBillDownloadUrl --cli-unfold-argument  \
    --Month 2023-12 \
    --FileType L3
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "",
        "Ready": 0,
        "RequestId": "1737bf56-fbb4-4a57-a08b-73901b74abf3"
    }
}
```

**Example 2: DescribeBillDownloadUrl-2**

子客获取自己的账单链接。文件已生成，请通过下载链接获取文件。

Input: 

```
tccli intlpartnersmgt DescribeBillDownloadUrl --cli-unfold-argument  \
    --Month 2024-12 \
    --FileType L2
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://xxxx.cos.ap-singapore.myqcloud.com/L3-bill_details.csv",
        "Ready": 1,
        "RequestId": "845ac46e-20a7-4cab-8930-d5e6d2104885"
    }
}
```

