**Example 1: 1**



Input: 

```
tccli rum DescribeTDEMSampleConfig --cli-unfold-argument  \
    --AppId 10
```

Output: 
```
{
    "Response": {
        "Result": "{\"AppId\":\"10\",\"Event\":{\"Enabled\":true,\"Types\":{}},\"Replay\":{\"Enabled\":false,\"ExperienceSampleRate\":0,\"ErrorTraceback\":false,\"ErrorSampleRate\":100},\"UpdatedAt\":null}",
        "RequestId": "3ee31b9c-5583-40dd-987c-51b38f4951b6"
    }
}
```

