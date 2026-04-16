**Example 1: 查询音色设计结果**



Input: 

```
tccli mps DescribeDesignTask --cli-unfold-argument  \
    --TaskId 1300057393-DesignVoiceAsync-88434eca-1484-4fcc-8589-e98027fc174e
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "Msg": "success",
        "Status": "success",
        "VoiceId": "v1_kuuEfwa/ADAozD26I/1sVcQgNNNj0egjBFWrvjnyqiaXzF8qfejCmOlUQc8n5Ss+CoRyMoYOrD3o9E0=",
        "RequestId": "5bf0e591-fadc-4b5f-9c9a-9586e09ec6af"
    }
}
```

