**Example 1: 克隆安全组**

克隆安全组

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-78ysaex1
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-4esrjvgl",
            "SecurityGroupName": "demo",
            "SecurityGroupDesc": "demo",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33",
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ],
            "UpdateTime": "2018-02-13 19:26:33",
            "IsDefault": false
        }
    }
}
```

**Example 2: 克隆安全组，指定项目ID**

克隆安全组，指定项目ID

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-78ysaex1 \
    --ProjectId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-2edhcclz",
            "SecurityGroupName": "demo",
            "SecurityGroupDesc": "demo",
            "ProjectId": "1001",
            "CreatedTime": "2018-01-13 19:26:33",
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ],
            "UpdateTime": "2018-02-13 19:26:33",
            "IsDefault": false
        }
    }
}
```

**Example 3: 克隆安全组，指定名称和备注**

克隆安全组，指定名称和备注

Input: 

```
tccli vpc CloneSecurityGroup --cli-unfold-argument  \
    --SecurityGroupId sg-78ysaex1 \
    --GroupName demo \
    --GroupDescription demo
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroup": {
            "SecurityGroupId": "sg-f42uhpkj",
            "SecurityGroupName": "demo",
            "SecurityGroupDesc": "demo",
            "ProjectId": "0",
            "CreatedTime": "2018-01-13 19:26:33",
            "TagSet": [
                {
                    "Key": "city",
                    "Value": "shanghai"
                }
            ],
            "UpdateTime": "2018-02-13 19:26:33",
            "IsDefault": false
        }
    }
}
```

