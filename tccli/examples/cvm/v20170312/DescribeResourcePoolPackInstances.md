**Example 1: 查询实例资源池内已创建的实例列表**

查询实例资源池内已创建的实例列表

Input: 

```
tccli cvm DescribeResourcePoolPackInstances --cli-unfold-argument  \
    --DedicatedResourcePackIds rpp-2gyonkx7
```

Output: 
```
{
    "Response": {
        "DedicatedResourcePackInstanceSet": [
            {
                "DedicatedResourcePackId": "rpp-2gyonkx7",
                "InstanceFamily": "S9",
                "InstanceIdSet": [
                    "ins-mmnxwk8y"
                ],
                "InstanceType": "S9.8XLARGE64",
                "Zone": "ap-guangzhou-7"
            }
        ],
        "RequestId": "f25c2f8b-cc99-430b-8cdd-905bfc56698e"
    }
}
```

