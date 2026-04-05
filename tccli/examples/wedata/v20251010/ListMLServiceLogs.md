**Example 1: MLServiceLogs**



Input: 

```
tccli wedata ListMLServiceLogs --cli-unfold-argument  \
    --Service INFER \
    --StartTime 2022-01-10T12:15:03+08:00 \
    --Limit 100 \
    --PodName ms-cp6rgw9r-1* \
    --EndTime 2022-01-11T12:15:03+08:00
```

Output: 
```
{
    "Response": {
        "Data": {
            "Content": [
                {
                    "Id": "77b5d420-73bc-47f2-96ab-3a2b32262ffe",
                    "Message": "This is a log",
                    "PodName": "ms-cp6rgw9r-1-864587bdb4-p5cv6",
                    "Timestamp": "2022-01-11T04:14:36.348499491Z"
                }
            ],
            "Context": "Y29udGV4dC0wYTdiNTRkMi0xOGI0LTQwNzEtYjIzYy1kZDE4NmM2NDFjNTIxNjQxODc0NTA2MTE5"
        },
        "RequestId": "305ce475-e534-4cad-a4ab-a472a27ca3fd"
    }
}
```

