**Example 1: demo**

demo

Input: 

```
tccli tcmpp DescribeMNPDetail --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --MNPId mp1mkdcf53ob2h8m
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPType": "Life Service->Lilliputian Services",
            "MNPName": "apiminiprogram",
            "MNPId": "mp1mkdcf53ob2h8m",
            "MNPIcon": "https://127.0.0.1/console/20240812101023-f1ae758593.jpeg",
            "MNPIntro": "api create mini program",
            "MNPDesc": "api create mini program",
            "Tags": null,
            "CreateUser": "murphypeng_mini",
            "CreateTime": 1723428625,
            "OnlineStatus": 0,
            "Applications": null,
            "Status": 0
        },
        "RequestId": "fc8c9245e37b49d3911ed0b38336c232"
    }
}
```

