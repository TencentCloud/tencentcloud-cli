**Example 1: 清除URL**



Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets http://www.qq.com/a.txt www.qq.com/1.txt \
    --Type purge_url \
    --ZoneId abc \
    --EncodeUrl True
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwch",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 清除abc站点下的所有资源**



Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Type purge_all \
    --ZoneId abc \
    --EncodeUrl True
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwch",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

