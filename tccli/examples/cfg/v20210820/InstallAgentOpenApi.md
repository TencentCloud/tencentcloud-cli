**Example 1: 示例**



Input: 

```
tccli cfg InstallAgentOpenApi --cli-unfold-argument  \
    --InstanceType 1 \
    --InstanceIds ins-********
```

Output: 
```
{
    "Response": {
        "Message": [
            "The current status of instance(s) ins-test001 is 卸载中, installation is not allowed."
        ],
        "RequestId": "fa8f4db3-f763-4c1d-aec7-8e1ca381c003"
    }
}
```

