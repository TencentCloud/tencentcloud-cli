**Example 1: Purging URLs**



Input: 

```
tccli ecdn PurgeUrlsCache --cli-unfold-argument  \
    --Urls http://www.test.com/1.jpg\
    --Area mainland
```

Output: 
```
{
    "Response": {
        "RequestId": "4d5a83f8-a61f-445b-8036-5636be640bef",
        "TaskId": "1533045796-i60rfmzm"
    }
}
```

