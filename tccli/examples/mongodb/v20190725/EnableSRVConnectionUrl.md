**Example 1: 开启实例SRV连接地址。**

开启成功，返回任务 ID。

Input: 

```
tccli mongodb EnableSRVConnectionUrl --cli-unfold-argument  \
    --InstanceId cmgo-gnu9vvnr
```

Output: 
```
{
    "Response": {
        "FlowId": 1709799293,
        "RequestId": "289f0372-6311-4679-9947-485d6de7c227"
    }
}
```

**Example 2: 开启实例的SRV访问地址。**

实例的SRV访问地址已开启。

Input: 

```
tccli mongodb EnableSRVConnectionUrl --cli-unfold-argument  \
    --InstanceId cmgo-gnu9vvnr
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "SRV connection has enabled."
        },
        "RequestId": "ad34dcec-b457-439f-8968-56109168efe2"
    }
}
```

