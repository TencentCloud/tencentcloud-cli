**Example 1: 修改VSM属性**

修改VSM属性

Input: 

```
tccli cloudhsm ModifyVsmAttributes --cli-unfold-argument  \
    --SgIds sg-abcdefgh \
    --VpcId vpc-abcdefgh \
    --ResourceId hsm-1234abcd \
    --SubnetId subnet-1234abcd \
    --ResourceName default-hsmName \
    --Type Default
```

Output: 
```
{
    "Response": {
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

