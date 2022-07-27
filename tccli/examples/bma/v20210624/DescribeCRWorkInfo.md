**Example 1: 查询作品基本信息**



Input: 

```
tccli bma DescribeCRWorkInfo --cli-unfold-argument  \
    --WorkId 111
```

Output: 
```
{
    "Response": {
        "MonitorStatus": 1,
        "IsProducer": 0,
        "WorkName": "xx",
        "RequestId": "xx",
        "AuthStatus": 1,
        "CommStatus": 1
    }
}
```

