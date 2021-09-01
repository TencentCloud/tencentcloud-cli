**Example 1: 获取样本分析结果**



Input: 

```
tccli habo DescribeStatus --cli-unfold-argument  \
    --Pk authkey \
    --Md5 md5_of_sample
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "Info": "success",
        "Data": "https://cloud.habo.qq.com/api/dl_report?md5=xxxxx&timeout=xxxxx&crc=xxxxx",
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6"
    }
}
```

