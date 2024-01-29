**Example 1: 请求demo**



Input: 

```
tccli wedata SubmitBatchTestRun --cli-unfold-argument  \
    --ProjectId 15316093243456467547465952 \
    --TaskIds 202312101212124564
```

Output: 
```
{
    "Response": {
        "BatchResult": [
            {
                "CurrRunDate": "20:12:12",
                "InstanceKey": "202312101212124564_20:12:12",
                "TaskId": "202312101212124564"
            }
        ],
        "RequestId": "be0c2a8d-e2e3-4a59-947d-83c6c901d16b"
    }
}
```

