**Example 1: 添加资产**



Input: 

```
tccli csip CreateDomainAndIp --cli-unfold-argument  \
    --Content abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Data": 0,
        "RequestId": "abc"
    }
}
```

