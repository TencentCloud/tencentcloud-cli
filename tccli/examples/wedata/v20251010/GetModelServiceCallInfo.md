**Example 1: GetModelServiceCallInfo**



Input: 

```
tccli wedata GetModelServiceCallInfo --cli-unfold-argument  \
    --ServiceId 8002380d-ba34-467c-b62e-aefe3d950b7e
```

Output: 
```
{
    "Response": {
        "Data": {
            "IntranetCallInfo": {
                "DefaultInnerCallInfos": null,
                "IngressPrivateLinkInfo": null,
                "PrivateLinkInfos": null,
                "PrivateLinkInfosV2": [],
                "ServiceEIPInfo": null
            },
            "ServiceCallInfo": {
                "AuthToken": "",
                "AuthorizationEnable": false,
                "InternetEndpoint": "https://ms-9vblq48gddguangzhou.ti.tencentcs.com/ms-9vblq48g",
                "ServiceGroupId": "msddd48g"
            }
        },
        "RequestId": "a1249845-3071-462cd d2096e7fda14"
    }
}
```

