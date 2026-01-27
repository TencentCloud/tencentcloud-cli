**Example 1: 修改实例的SRV连接地址的TTL时间。**

修改成功，返回任务 ID。

Input: 

```
tccli mongodb ModifySRVConnectionUrl --cli-unfold-argument  \
    --InstanceId cmgo-gnu9vvnr \
    --CustomDomain myinstancedomain
```

Output: 
```
{
    "Response": {
        "FlowId": 1709799294,
        "RequestId": "e799e11c-c615-49c0-8b24-67b5fb45820f"
    }
}
```

