**Example 1: 创建批量创建设备任务示例**



Input: 

```
tccli iotcloud CreateMultiDevicesTask --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --ParametersType random \
    --BatchCount 1
```

Output: 
```
{
    "Response": {
        "Id": 1000001,
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

