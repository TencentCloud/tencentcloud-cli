**Example 1: 清除abc站点下的所有资源**



Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Type purge_all \
    --ZoneId zone-ajj243dwrew \
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

**Example 2: 清除URL**



Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets http://www.qq.com/a.txt \
    --Type purge_url \
    --ZoneId zone-ajj243dwrew \
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

