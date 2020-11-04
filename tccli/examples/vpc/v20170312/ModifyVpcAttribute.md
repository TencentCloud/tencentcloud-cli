**Example 1: 修改VPC属性**



Input: 

```
tccli vpc ModifyVpcAttribute --cli-unfold-argument  \
    --Version 2017-03-12\
    --VpcName MyTest\
    --VpcId vpc-m7sr81gh\
    --EnableMulticast true
```

Output: 
```
{
    "Response": {
        "RequestId": "38b1a253-02b7-43d7-8524-7e07432ae31a"
    }
}
```

