**Example 1: GetCrowdPackList**



Input: 

```
tccli zj GetCrowdPackList --cli-unfold-argument  \
    --Name aaa \
    --Status -1 \
    --Offset 0 \
    --Limit -1 \
    --License xsdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 14,
            "List": [
                {
                    "ID": 68,
                    "CreatedAt": "2020-01-03T11:15:22+08:00",
                    "Name": "test",
                    "Status": 2,
                    "PhoneNum": 11,
                    "Tag": "aaa",
                    "MD5": "088a2a5ac1961e79dc7a55cac59a6d67",
                    "FileName": "1bdcb971-f57a-4c9b-98eb-46c64ba1cf98.txt",
                    "Desc": ""
                }
            ]
        },
        "RequestId": "111111"
    }
}
```

