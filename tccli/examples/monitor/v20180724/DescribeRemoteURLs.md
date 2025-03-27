**Example 1: 获取多写配置**

获取多写配置

Input: 

```
tccli monitor DescribeRemoteURLs --cli-unfold-argument  \
    --InstanceId prom-kewhrgvf \
    --RemoteURLs http://172.0.0.1:9090/api/v1/prom/write
```

Output: 
```
{
    "Response": {
        "RemoteWrites": [
            {
                "URL": "http://172.0.0.1:9090/api/v1/prom/write",
                "URLRelabelConfig": "source_labels:asd\n",
                "BasicAuth": {
                    "UserName": "user-name",
                    "Password": "sklehrgb"
                },
                "MaxBlockSize": "1024",
                "Label": "label-name=label-value",
                "Headers": [
                    {
                        "Key": "X-Custom-Header",
                        "Value": "custom-value"
                    }
                ]
            }
        ],
        "RequestId": "langy-akrbnf"
    }
}
```

