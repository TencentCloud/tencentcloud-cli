**Example 1: 开通集群只读组接入地址**

任何场景

Input: 

```
tccli cynosdb OpenClusterReadOnlyInstanceGroupAccess --cli-unfold-argument  \
    --ClusterId cynosdbmysql-abcd1234 \
    --Port 3306 \
    --SecurityGroupIds SecurityGroupIds1 SecurityGroupIds2
```

Output: 
```
{
    "Response": {
        "FlowId": 147287,
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

