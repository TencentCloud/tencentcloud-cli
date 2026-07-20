**Example 1: 删除推理服务**



Input: 

```
tccli teo OperateInferenceService --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --ServiceId inf-9f8***4a3210 \
    --Operation Delete
```

Output: 
```
{
    "Response": {
        "RequestId": "d8421228-6851-4b2c-bff0-a1c415c48ced"
    }
}
```

**Example 2: 启动推理服务**



Input: 

```
tccli teo OperateInferenceService --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --ServiceId inf-9f8***4a3210 \
    --Operation Resume
```

Output: 
```
{
    "Response": {
        "RequestId": "cbabe886-9d89-4333-a815-a44f6ffe2604"
    }
}
```

**Example 3: 停止推理服务**



Input: 

```
tccli teo OperateInferenceService --cli-unfold-argument  \
    --ZoneId zone-2***8ev000 \
    --ServiceId inf-9f8***4a3210 \
    --Operation Stop
```

Output: 
```
{
    "Response": {
        "RequestId": "c78690b2-ece1-4fc6-b03e-8ea6c56c2bdc"
    }
}
```

