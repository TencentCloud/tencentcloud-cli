**Example 1: 设置实例SSL状态**

关闭SSL状态示例

Input: 

```
tccli mongodb InstanceEnableSSL --cli-unfold-argument  \
    --InstanceId cmgo-eqmoaxxx \
    --Enable true
```

Output: 
```
{
    "Response": {
        "CertUrl": "https://cert-****",
        "ExpiredTime": "2024-03-29 13:40:56",
        "RequestId": "5297ebe2-63f8-465f-be7d-41058ce438",
        "Status": 1
    }
}
```

