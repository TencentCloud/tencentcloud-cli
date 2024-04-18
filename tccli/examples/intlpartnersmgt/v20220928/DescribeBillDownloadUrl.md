**Example 1: DescribeBillDownloadUrl**

用于子客下载账单文件，返回账单文件url

	
POST / HTTP/1.1
Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeBillDownloadUrl

Input: 

```
tccli intlpartnersmgt DescribeBillDownloadUrl --cli-unfold-argument  \
    --Month 2023-10 \
    --FileType L3
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "https://xxxx.cos.ap-singapore.myqcloud.com/L3-bill_details.csv",
        "RequestId": "abc"
    }
}
```

