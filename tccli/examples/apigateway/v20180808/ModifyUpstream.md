**Example 1: 修改vpc通道信息**



Input: 

```
tccli apigateway ModifyUpstream --cli-unfold-argument  \
    --UpstreamId upstream-0c96l2bo \
    --Retries 4 \
    --UpstreamName test \
    --UpstreamHost www.a.com \
    --UpstreamDescription test
```

Output: 
```
{
    "Response": {
        "Result": {
            "Retries": 1,
            "Algorithm": "xx",
            "UniqVpcId": "xx",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "UpstreamId": "xx",
            "UpstreamName": "xx",
            "UpstreamDescription": "xx",
            "Nodes": [
                {
                    "VmInstanceId": "xx",
                    "Host": "xx",
                    "Port": 1,
                    "Weight": 1,
                    "Tags": [
                        "xx"
                    ]
                }
            ],
            "Scheme": "xx"
        },
        "RequestId": "xx"
    }
}
```

