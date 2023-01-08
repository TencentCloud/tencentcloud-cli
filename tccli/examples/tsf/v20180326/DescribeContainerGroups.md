**Example 1: 查询容器部署组列表**

查询容器部署组列表

Input: 

```
tccli tsf DescribeContainerGroups --cli-unfold-argument  \
    --ApplicationId application-xxxxxxx \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "41a08459-9e0b-4609-841b-0859d6f844e1",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "Server": "ccr.ccs.tencentyun.com",
                    "CpuLimit": "2.00",
                    "GroupId": "group-xxxxxxx",
                    "ClusterId": "cls-xxxxxxx",
                    "TagName": "20190517xxxxxxx",
                    "CpuRequest": "",
                    "MemLimit": "4096.00",
                    "GroupName": "test",
                    "CreateTime": "",
                    "NamespaceId": "namespace-xxxxxxx",
                    "MemRequest": "",
                    "ClusterName": "示例",
                    "NamespaceName": "test"
                }
            ]
        }
    }
}
```

