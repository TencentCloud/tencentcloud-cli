**Example 1: 示例**

示例

Input: 

```
tccli trocket ModifyMQTTInsPublicEndpoint --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --Bandwidth 2 \
    --Rules.0.IpRule 2.2.2.2 \
    --Rules.0.Allow True \
    --Rules.0.Remark 555
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "02eb3529-3440-44e9-b2c8-1e65c7017c09"
    }
}
```

