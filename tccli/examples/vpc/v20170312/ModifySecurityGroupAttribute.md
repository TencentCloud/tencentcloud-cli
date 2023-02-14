**Example 1: 修改安全组属性**

修改安全组属性

Input: 

```
tccli vpc ModifySecurityGroupAttribute --cli-unfold-argument  \
    --SecurityGroupId sg-33ocnj9n \
    --GroupName TestGroupNewName \
    --GroupDescription test-group-desc
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

