**Example 1: 修改自动策略名称**



Input: 

```
tccli cfs ModifyAutoDeletePolicy --cli-unfold-argument  \
    --FileSystemId cfs-4e5e7**** \
    --PolicyId adp-d774**** \
    --PolicyName te***
```

Output: 
```
{
    "Response": {
        "RequestId": "49c5456f-038f-4daf-bbdf-678ac32ba0a9"
    }
}
```

**Example 2: 修改自动策略名称和路径**



Input: 

```
tccli cfs ModifyAutoDeletePolicy --cli-unfold-argument  \
    --FileSystemId cfs-4e5e7**** \
    --PolicyId adp-d774**** \
    --Paths /cfs/* \
    --PolicyName te***
```

Output: 
```
{
    "Response": {
        "RequestId": "b4a8dab3-ed49-44d1-b5a8-745f9af36190"
    }
}
```

**Example 3: 修改自动策略路径**



Input: 

```
tccli cfs ModifyAutoDeletePolicy --cli-unfold-argument  \
    --FileSystemId cfs-4e5e7**** \
    --PolicyId adp-d774**** \
    --Paths /cfs/*
```

Output: 
```
{
    "Response": {
        "RequestId": "5a633af9-42b8-4e41-babd-8056aa77fd1e"
    }
}
```

