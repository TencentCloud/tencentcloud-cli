**Example 1: 查询GPU服务器**

查询GPU服务器

Input: 

```
tccli ihn DescribeRdmaServers --cli-unfold-argument  \
    --ModuleId 818181 \
    --ClusterId 8888 \
    --InstanceUuids 075c288a-cd57-4906-b1fb-f2fd6f9f36b2 \
    --ClusterInfo.ClusterType 1 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RdmaServers": [
            {
                "AutoIsolate": false,
                "ClusterId": 8888,
                "GatewayIp": "192.81.1.157",
                "InstanceUuid": "075c288a-cd57-4906-b1fb-f2fd6f9f36b2",
                "IntMask": 30,
                "Mask": "255.255.255.252",
                "ModuleId": 818181,
                "ServerIp": "192.81.1.158",
                "Subnet": "192.81.1.156"
            }
        ],
        "TotalCount": 1,
        "RequestId": "44ac5915-8a61-4775-bee1-814deadea13c"
    }
}
```

**Example 2: 查询IB机型服务器**

查询IB机型服务器

Input: 

```
tccli ihn DescribeRdmaServers --cli-unfold-argument  \
    --ModuleId 919191 \
    --ClusterId 9999 \
    --InstanceUuids cb9da3ec-e96e-4fab-ad85-e96e4fabad85 \
    --ClusterInfo.ClusterType 2 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RdmaServers": [
            {
                "ClusterId": 9999,
                "GUID": "491a7f3c47145acf",
                "InstanceUuid": "cb9da3ec-e96e-4fab-ad85-e96e4fabad85",
                "ModuleId": 919191,
                "PKeyId": 1
            }
        ],
        "TotalCount": 2,
        "RequestId": "8a68b5ef-3919-4e28-b4f4-14034fbf116d"
    }
}
```

