**Example 1: 单卡机器查申请IP异步任务信息**

单卡机器查申请IP异步任务信息

Input: 

```
tccli ihn DescribeVpcTaskResult --cli-unfold-argument  \
    --TaskId dd214b4d-fe3d-498b-9851-d1dad89832c4
```

Output: 
```
{
    "Response": {
        "Output": {
            "ClusterId": 8888,
            "GatewayIp": "192.81.1.189",
            "InstanceUuid": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
            "IntMask": 30,
            "Mask": "255.255.255.252",
            "ModuleId": 818181,
            "ServerIp": "192.81.1.190",
            "Subnet": "192.81.1.188"
        },
        "Status": "SUCCESS",
        "RequestId": "0addb58a-0861-4dd5-9ee2-155edadea1bf"
    }
}
```

**Example 2: 多卡机器查申请IP异步任务信息**

多卡机器查申请IP异步任务信息

Input: 

```
tccli ihn DescribeVpcTaskResult --cli-unfold-argument  \
    --TaskId 79a67e57-e6f9-48cd-b29c-fa6fb1db1edb
```

Output: 
```
{
    "Response": {
        "RequestId": "dfb91b83-7aca-46d5-a740-683ae65ca39b",
        "Result": [
            {
                "Output": "{\"ClusterId\": 8888, \"GatewayIp\": \"192.81.1.173\", \"InstanceUuid\": \"075c288a-cd57-4906-b1fb-f2fd6f9f36c3\", \"IntMask\": 30, \"Mask\": \"255.255.255.252\", \"ModuleId\": 818181, \"ServerIp\": \"192.81.1.174\", \"Subnet\": \"192.81.1.172\"}",
                "ResourceId": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
                "Status": "SUCCESS"
            },
            {
                "Output": "{\"ClusterId\": 8888, \"GatewayIp\": \"192.81.1.193\", \"InstanceUuid\": \"075c288a-cd57-4906-b1fb-f2fd6f9f36c3\", \"IntMask\": 30, \"Mask\": \"255.255.255.252\", \"ModuleId\": 818181, \"ServerIp\": \"192.81.1.194\", \"Subnet\": \"192.81.1.192\"}",
                "ResourceId": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
                "Status": "SUCCESS"
            },
            {
                "Output": "{\"ClusterId\": 8888, \"GatewayIp\": \"192.81.1.181\", \"InstanceUuid\": \"075c288a-cd57-4906-b1fb-f2fd6f9f36c3\", \"IntMask\": 30, \"Mask\": \"255.255.255.252\", \"ModuleId\": 818181, \"ServerIp\": \"192.81.1.182\", \"Subnet\": \"192.81.1.180\"}",
                "ResourceId": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
                "Status": "SUCCESS"
            },
            {
                "Output": "{\"ClusterId\": 8888, \"GatewayIp\": \"192.81.1.177\", \"InstanceUuid\": \"075c288a-cd57-4906-b1fb-f2fd6f9f36c3\", \"IntMask\": 30, \"Mask\": \"255.255.255.252\", \"ModuleId\": 818181, \"ServerIp\": \"192.81.1.178\", \"Subnet\": \"192.81.1.176\"}",
                "ResourceId": "075c288a-cd57-4906-b1fb-f2fd6f9f36c3",
                "Status": "SUCCESS"
            }
        ],
        "Status": "SUCCESS"
    }
}
```

**Example 3: 查创建服务器、删除服务器等任务信息**

查创建服务器、删除服务器等任务信息

Input: 

```
tccli ihn DescribeVpcTaskResult --cli-unfold-argument  \
    --TaskId fa8d6a33-2576-447f-b993-d8bb7df9c4db
```

Output: 
```
{
    "Response": {
        "Status": "SUCCESS",
        "RequestId": "e06d0285-4910-43b0-9965-80c1daa3597e"
    }
}
```

