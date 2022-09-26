**Example 1: QueryFinancialDataUrl**

查询金融数据文件下载链接

Input: 

```
tccli cpdp QueryFinancialDataUrl --cli-unfold-argument  \
    --DataType INVOICE \
    --StartTime 2022-02-01 00:00:00 \
    --EndTime 2022-02-28 23:59:59
```

Output: 
```
{
    "Response": {
        "CosUrl": "xxxxx",
        "ExpireTime": "2022-06-07 00:00:00",
        "RequestId": "8ffecac1-2d89-43a9-9075-a985442ef466"
    }
}
```

