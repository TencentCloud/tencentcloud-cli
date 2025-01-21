**Example 1: 查询节点信息**



Input: 

```
tccli cdwdoris DescribeInstanceNodesInfo --cli-unfold-argument  \
    --InstanceID cdwdoris-xxx
```

Output: 
```
{
    "Response": {
        "BeNodes": [
            "str"
        ],
        "FeNodes": [
            "str"
        ],
        "FeMaster": "str",
        "RequestId": "str"
    }
}
```

**Example 2: 查询节点角色**

查询节点角色

Input: 

```
tccli cdwdoris DescribeInstanceNodesInfo --cli-unfold-argument  \
    --InstanceID cdwdoris-xxx
```

Output: 
```
{
    "Response": {
        "BeNodes": [
            "str"
        ],
        "FeNodes": [
            "str"
        ],
        "FeMaster": "str",
        "RequestId": "str"
    }
}
```

