**Example 1: Sample request**



Input: 

```
tccli mdl CreateMediaLiveInput --cli-unfold-argument  \
    --Name sdad \
    --Type RTMP_PUSH \
    --SecurityGroupIds 123 \
    --InputSettings.0.AppName live \
    --InputSettings.0.StreamName test
```

Output: 
```
{
    "Response": {
        "Id": 111,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

