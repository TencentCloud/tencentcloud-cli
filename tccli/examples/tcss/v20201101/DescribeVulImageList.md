**Example 1: 查询漏洞影响的镜像列表**



Input: 

```
tccli tcss DescribeVulImageList --cli-unfold-argument  \
    --PocID 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ComponentList": [
                    {
                        "FixedVersion": ">6.0.37,>8.0.0",
                        "Name": "catalina",
                        "Path": "tomcat7/apache-tomcat-7.0.34/lib/catalina.jar",
                        "Version": "7.0.34"
                    }
                ],
                "ContainerCount": 0,
                "HostCount": 1,
                "SuperNodeCount": 1,
                "ImageID": "sha256:5e1476716a780a0bf6d4776d02840254257a6c0711fe0e17a7d693aba0dff8fb",
                "ImageName": "image"
            }
        ],
        "RequestId": "940b7fab-b4fc-4740-a719-6c1dd122af3f",
        "TotalCount": 1
    }
}
```

