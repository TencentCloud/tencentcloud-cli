**Example 1: CreateRight**



Input: 

```
tccli cpp CreateRight --cli-unfold-argument  \
    --TaskName abc \
    --WorkId abc \
    --AuthList.0.AuthUrl abc \
    --AuthList.0.ValidStartDate abc \
    --AuthList.0.ValidEndDate abc \
    --InfringeIdList 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskId": "abc",
            "Letters": [
                {
                    "LetterId": "abc",
                    "InfringeId": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

