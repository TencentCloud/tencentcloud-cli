**Example 1: 重启应用实例**

重启应用实例

Input: 

```
tccli tem RestartApplicationPod --cli-unfold-argument  \
    --Status xx \
    --EnvironmentId xx \
    --Offset 0 \
    --SourceChannel 0 \
    --Limit 0 \
    --PodName xx \
    --ApplicationId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

