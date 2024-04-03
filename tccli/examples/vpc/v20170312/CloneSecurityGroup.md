**Example 1: 克隆安全组**

克隆安全组

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12341234",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33"
        }
    }
}
```

**Example 2: 克隆安全组，指定项目ID**

克隆安全组，指定项目ID

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-12345678 \
    --ProjectId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12341278",
            "SecurityGroupName": "TestGroup",
            "SecurityGroupDesc": "test-group-desc",
            "ProjectId": "1001",
            "CreatedTime": "2018-01-13 19:26:33"
        }
    }
}
```

**Example 3: 克隆安全组，指定名称和备注**

克隆安全组，指定名称和备注

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-12345678 \
    --GroupName test \
    --GroupDescription test
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-12341256",
            "SecurityGroupName": "test",
            "SecurityGroupDesc": "test",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33"
        }
    }
}
```

