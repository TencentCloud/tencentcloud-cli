**Example 1: SendTrafficSecuritySmsMessage**



Input: 

```
tccli taf SendTrafficSecuritySmsMessage --cli-unfold-argument  \
    --BspData.TaskId 4128\
    --BspData.Mobiles 1382350**** 1382351****
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Value": []
        },
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

