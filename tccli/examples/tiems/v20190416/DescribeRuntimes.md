**Example 1: 描述服务运行环境**



Input: 

```
tccli tiems DescribeRuntimes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "efcdba3f-080f-4913-a7a2-5f47e0baf67a",
        "Runtimes": [
            {
                "Name": "pmml",
                "Framework": "pmml",
                "Description": "pmml-description",
                "Public": true,
                "HealthCheckOn": true,
                "Image": "**",
                "CreateTime": "2019-11-01T17:03:26+08:00"
            },
            {
                "Name": "angel",
                "Framework": "angel",
                "Description": "angel-description",
                "Public": true,
                "HealthCheckOn": true,
                "Image": "**",
                "CreateTime": "2019-11-01T17:03:26+08:00"
            },
            {
                "Name": "tfserving",
                "Framework": "tfserving",
                "Description": "tfserving-description",
                "Public": true,
                "HealthCheckOn": true,
                "Image": "**",
                "CreateTime": "2019-11-01T17:03:26+08:00"
            },
            {
                "Name": "test",
                "Framework": "test",
                "Description": "字符串",
                "Public": false,
                "HealthCheckOn": false,
                "Image": "ccr.ccs.tencentyun.com/mla-library/tool",
                "CreateTime": "2019-11-07T14:47:49+08:00"
            }
        ],
        "UserAccess": 1
    }
}
```

