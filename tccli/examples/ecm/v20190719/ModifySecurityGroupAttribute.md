**Example 1: 修改安全组属性**



Input: 

```
tccli ecm ModifySecurityGroupAttribute --cli-unfold-argument  \
    --Version 2019-07-19 \
    --SecurityGroupId esg-33ocnj9n \
    --GroupName TestGroupNewName \
    --GroupDescription test-group-desc
```

Output: 
```
{
    "Response": {}
}
```

