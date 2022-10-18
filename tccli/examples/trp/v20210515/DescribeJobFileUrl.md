**Example 1: 获取异步任务的输出地址**



Input: 

```
tccli trp DescribeJobFileUrl --cli-unfold-argument  \
    --JobId 1000
```

Output: 
```
{
    "Response": {
        "Url": "https://anxin-private-1251316161.cos.ap-guangzhou.myqcloud.com/anxin/1d8-4460-a039.zip",
        "RequestId": "d8dca787-f07a-40ce-acd5-3c0eda11cac2"
    }
}
```

