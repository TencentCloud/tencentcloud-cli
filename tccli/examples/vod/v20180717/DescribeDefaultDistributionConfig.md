**Example 1: 查询默认分发配置**

查询默认分发配置。

Input: 

```
tccli vod DescribeDefaultDistributionConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "requestId",
        "Domain": "test.vod2.myqcluod.com",
        "DomainName": "test.vod2.myqcluod.com",
        "Scheme": "HTTPS",
        "PlayKey": "abc12342a"
    }
}
```

