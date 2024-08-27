**Example 1: ex:**

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
        "FlowId": "12345",
        "RequestId": "qwertyuiop"
    }
}
```

