**Example 1: 新增待扫描站点**

新增站点用于漏洞扫描或漏洞监测

Input: 

```
tccli cws CreateSites --cli-unfold-argument  \
    --Urls http%3A%2F%2Fwww.qcloud.com \
    --UserAgent Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_13_4)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F66.0.3359.139%20Safari%2F537.36
```

Output: 
```
{
    "Response": {
        "Number": 1,
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Sites": [
            {
                "SiteId": 4402,
                "Url": "http://demo.aisec.cn/demo/aisec/testb"
            }
        ]
    }
}
```

