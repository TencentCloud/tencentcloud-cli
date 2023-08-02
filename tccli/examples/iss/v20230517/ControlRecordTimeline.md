**Example 1: 成功**

 

Input: 

```
tccli iss ControlRecordTimeline --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890ab \
    --Start 1685611685 \
    --End 1685611785
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Begin": 1687276800,
                "End": 1687278194
            }
        ],
        "RequestId": "57c7a6c6-8334-450b-9a57-4c2c2a6e26d2"
    }
}
```

**Example 2: 无本地录像结果**

 

Input: 

```
tccli iss ControlRecordTimeline --cli-unfold-argument  \
    --ChannelId 12345678-abcd-efgh-ijkl-1234567890ab \
    --Start 1685611685 \
    --End 1685611785
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "57c7a6c6-8334-450b-9a57-4c2c2a6e26d2"
    }
}
```

