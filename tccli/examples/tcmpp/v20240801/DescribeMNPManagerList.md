**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPManagerList --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --Keyword  \
    --TeamId 6519624807 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "DataList": [
                {
                    "MNPId": "mp1mkdcf53ob2h8m",
                    "MNPName": "apiminiprogram",
                    "MNPIcon": "https://127.0.0.1/console/20240812101023-f1ae758593.jpeg",
                    "TeamName": "MiniApp",
                    "AccessStatus": 0,
                    "Status": 0
                }
            ]
        },
        "RequestId": "a25029ca836e4d33b085717b7107645a"
    }
}
```

