**Example 1: 查询节点信息**



Input: 

```
tccli cdwdoris DescribeInstanceNodesInfo --cli-unfold-argument  \
    --InstanceID abc
```

Output: 
```
{
    "Response": {
        "BeNodes": [
            "abc"
        ],
        "FeNodes": [
            "abc"
        ],
        "FeMaster": "abc",
        "RequestId": "abc"
    }
}
```

**Example 2: 查询节点角色**

查询节点角色

Input: 

```
tccli cdwdoris DescribeInstanceNodesInfo --cli-unfold-argument  \
    --InstanceID abc
```

Output: 
```
{
    "Response": {
        "BeNodes": [
            "abc"
        ],
        "FeNodes": [
            "abc"
        ],
        "FeMaster": "abc",
        "RequestId": "abc"
    }
}
```

