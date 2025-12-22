**Example 1: success**



Input: 

```
tccli tcbr DescribeCloudRunDeployRecord --cli-unfold-argument  \
    --ServerName 字符串 \
    --EnvId 字符串
```

Output: 
```
{
    "Response": {
        "DeployRecords": [],
        "RequestId": "66038a58-061f-49a2-a5fd-b8cf00795ffb"
    }
}
```

**Example 2: DescribeCloudRunDeployRecord**



Input: 

```
tccli tcbr DescribeCloudRunDeployRecord --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc
```

Output: 
```
{
    "Response": {
        "DeployRecords": [
            {
                "DeployId": "abc",
                "DeployTime": "abc",
                "Status": "abc",
                "RunId": "abc",
                "BuildId": 0,
                "FlowRatio": 0,
                "ImageUrl": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

