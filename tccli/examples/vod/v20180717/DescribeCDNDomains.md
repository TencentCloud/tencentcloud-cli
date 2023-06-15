**Example 1: 查询所有CDN域名**

查询所有CDN域名

Input: 

```
tccli vod DescribeCDNDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DomainSet": [
            {
                "Domain": "myexample.com",
                "DeployStatus": "online",
                "CreateTime": "2022-01-01T00:00:00+08:00",
                "Config": {
                    "Area": "mainland",
                    "Origin": {
                        "Origins": [
                            "src.myexample.com"
                        ],
                        "OriginType": "domain"
                    }
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "12ae8d8e-dce3-4551-9d4b-5594145287e"
    }
}
```

