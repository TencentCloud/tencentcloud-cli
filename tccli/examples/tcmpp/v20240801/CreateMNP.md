**Example 1: CreateMNP**



Input: 

```
tccli tcmpp CreateMNP --cli-unfold-argument  \
    --PlatformId T02245JR9111721GKOI \
    --TeamId 6519624807 \
    --MNPName apiminiprogram \
    --MNPType Life Service->144_Lilliputian Services \
    --MNPIntro api create mini program \
    --MNPDesc api create mini program \
    --MNPIcon https://127.0.0.1/console/20240812101023-f1ae758593.jpeg
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": "mp1mkdcf53ob2h8m"
        },
        "RequestId": "e5b444cb698246b6852bd980114ca151"
    }
}
```

