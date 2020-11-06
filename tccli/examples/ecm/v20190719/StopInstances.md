**Example 1: 实例关机**

实例关机

Input: 

```
tccli ecm StopInstances --cli-unfold-argument  \
    --InstanceIdSet ein-496721al ein-438242bp \
    --ForceStop false \
    --StopType SOFT_FIRST
```

Output: 
```
{
    "Response": {
        "RequestId": "d40cdb72-7bc0-4b48-b3aa-25e8401f6999"
    }
}
```

