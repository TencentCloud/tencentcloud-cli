**Example 1: 示例**

示例

Input: 

```
tccli trocket CreateMQTTInsPublicEndpoint --cli-unfold-argument  \
    --InstanceId mqtt-rvb5xxrn \
    --Bandwidth 2 \
    --Rules.0.IpRule 1.1.1.1 \
    --Rules.0.Allow True \
    --Rules.0.Remark remark
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "416510a6-f614-487d-bbca-e7fdbf72fc29"
    }
}
```

