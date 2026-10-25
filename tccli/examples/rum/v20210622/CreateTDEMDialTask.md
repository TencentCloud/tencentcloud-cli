**Example 1: 创建拨测任务**

创建一个按固定频率执行的 ICMP 拨测任务。

Input: 

```
tccli rum CreateTDEMDialTask --cli-unfold-argument  \
    --AppId 5 \
    --TaskName capi-selftest-0930 \
    --Type icmp \
    --ExecutionTime realtime \
    --TimeoutMs 3000 \
    --PeriodMs 60000 \
    --PackageCount 3 \
    --DialDomain www.qq.com \
    --FrequencyMs 60000 \
    --PackageSize 64
```

Output: 
```
{
    "Response": {
        "RequestId": "c2089c4d-6e56-456e-80d0-908a4a01b91c"
    }
}
```

