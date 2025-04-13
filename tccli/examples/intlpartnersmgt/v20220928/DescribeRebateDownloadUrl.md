**Example 1: DescribeRebateDownloadUrl**

经销商/代理商获取月返佣账单文件链接。文件已生成，请通过下载链接获取文件。

Input: 

```
tccli intlpartnersmgt DescribeRebateDownloadUrl --cli-unfold-argument  \
    --Month 2024-12 \
    --FileType CommissionDetail
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://xxxx.cos.ap-singapore.myqcloud.com",
        "Ready": 1,
        "RequestId": "845ac46e-20a7-4cab-8930-d5e6d2104885"
    }
}
```

