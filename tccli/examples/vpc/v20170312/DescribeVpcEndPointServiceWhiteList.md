**Example 1: 查询终端节点服务的服务白名单列表**

查询终端节点服务的服务白名单列表

Input: 

```
tccli vpc DescribeVpcEndPointServiceWhiteList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpcEndpointServiceUserSet": [
            {
                "Owner": 1254277469,
                "UserUin": "100016184089",
                "Description": "描述信息",
                "EndPointServiceId": "",
                "CreateTime": "vpcsvc-kngiybxl"
            }
        ],
        "RequestId": "7e6f5074-e4a2-4bb6-9cac-d2357a00896f"
    }
}
```

