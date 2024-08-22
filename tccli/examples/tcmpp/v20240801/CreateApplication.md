**Example 1: CreateApplication**



Input: 

```
tccli tcmpp CreateApplication --cli-unfold-argument  \
    --ApplicationName test \
    --Logo http://127.0..0.1/T04257DS9431720WTAG/console/20240819193433-a67c2b912e.png \
    --PlatformId T04257DS9431720WTAG \
    --AndroidAppKey com.test \
    --IosAppKey com.test \
    --Intro test \
    --Remark testtest \
    --TeamId 9213128346 \
    --ApplicationType 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ResourceId": "app-0lcjnpmdpr"
        },
        "RequestId": "b4bbc366-892c-4ec2-9edc-2a572c1770b4"
    }
}
```

