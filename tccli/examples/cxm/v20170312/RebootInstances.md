**Example 1: 重启实例**

重启实例

Input: 

```
tccli cxm RebootInstances --cli-unfold-argument  \
    --InstanceIds eks-e9jeu72o \
    --StopType HARD
```

Output: 
```
{
    "Response": {
        "RequestId": "b9211458-17d2-4539-8a5c-e123b85ac819",
        "TaskId": 283426327
    }
}
```

