**Example 1: BuildMessageRoute**



Input: 

```
tccli iecp BuildMessageRoute --cli-unfold-argument  \
    --SourceUnitIDList 0 \
    --TopicFilter 0event \
    --Descript  \
    --RouteName test \
    --SourceDeviceNameList link02 \
    --Mode topic-datasource \
    --SourceProductID SA4RZ3NLIM
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3"
    }
}
```

