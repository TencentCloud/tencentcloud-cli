**Example 1: 部署生效**



Input: 

```
tccli emr ModifyYarnDeploy --cli-unfold-argument  \
    --InstanceId emr-a903oah8 \
    --OldScheduler capacity \
    --NewScheduler fair
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "ErrorMsg",
        "IsDraft": false,
        "RequestId": "d76bd103-947e-49f3-8485-e6aab28ecbbf"
    }
}
```

