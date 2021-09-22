**Example 1: 导出风险趋势**



Input: 

```
tccli cwp ExportSecurityTrends --cli-unfold-argument  \
    --BeginDate 2020-06-01 \
    --EndDate 2020-06-10
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "DownloadUrl": "http://download.url/xxx.csv"
    }
}
```

