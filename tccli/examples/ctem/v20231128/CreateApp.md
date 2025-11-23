**Example 1: 添加APP资产**

添加APP资产

Input: 

```
tccli ctem CreateApp --cli-unfold-argument  \
    --CustomerId 100081 \
    --Name test \
    --Platform android \
    --AppVersion v1.1.1 \
    --DownloadUrl http://a.test.com \
    --PackageName com.test \
    --Developer tester \
    --ServerUrl http://test.com \
    --Description test
```

Output: 
```
{
    "Response": {
        "Id": 11,
        "RequestId": "6b4c2d18-d8e5-4a65-8eb4-0a90cb4c488b"
    }
}
```

