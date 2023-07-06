**Example 1: 预热URL**

提交预热任务。

Input: 

```
tccli teo CreatePrefetchTask --cli-unfold-argument  \
    --Targets http://www.qq.com/a.txt \
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

