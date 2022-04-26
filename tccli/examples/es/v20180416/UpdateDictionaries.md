**Example 1: 更新ES集群词典**



Input: 

```
tccli es UpdateDictionaries --cli-unfold-argument  \
    --IkStopwords xx \
    --Synonym xx \
    --InstanceId xx \
    --UpdateType 0 \
    --ForceRestart True \
    --QQDict xx \
    --IkMainDicts xx
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

