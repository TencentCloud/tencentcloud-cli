**Example 1: 更新ES集群词典**

更新ES集群词典

Input: 

```
tccli es UpdateDictionaries --cli-unfold-argument  \
    --IkStopwords abc \
    --Synonym abc \
    --InstanceId abc \
    --UpdateType 0 \
    --ForceRestart True \
    --QQDict abc \
    --IkMainDicts abc
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

