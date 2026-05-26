**Example 1: 1**



Input: 

```
tccli tdmysql DescribeUserPrivileges --cli-unfold-argument  \
    --UserName qt4s_test \
    --InstanceId tdsql3-0b2f04e0 \
    --Object sbtest10 \
    --Host % \
    --DbName test \
    --ObjectType table
```

Output: 
```
{
    "Response": {
        "Privileges": [],
        "RequestId": "40b596e8-0b33-48ce-bd61-a2a5891a0920"
    }
}
```

**Example 2: 123**



Input: 

```
tccli tdmysql DescribeUserPrivileges --cli-unfold-argument  \
    --UserName 字符串 \
    --InstanceId tdsql3-267841d2 \
    --Object 字符串 \
    --ColName 字符串 \
    --Host % \
    --DbName 字符串 \
    --ObjectType 字符串
```

Output: 
```
{
    "Response": {
        "Privileges": [],
        "RequestId": "cae0499f-194e-4fec-a46a-9c42eaaeb753"
    }
}
```

**Example 3: 321**



Input: 

```
tccli tdmysql DescribeUserPrivileges --cli-unfold-argument  \
    --UserName 字符串 \
    --InstanceId tdsql3-267841d2 \
    --Object 字符串 \
    --ColName 字符串 \
    --Host % \
    --DbName 字符串 \
    --ObjectType 字符串
```

Output: 
```
{
    "Response": {
        "Privileges": [],
        "RequestId": "7ac86126-4006-43aa-9dad-267e2f5ff0d8"
    }
}
```

**Example 4: null**



Input: 

```
tccli tdmysql DescribeUserPrivileges --cli-unfold-argument  \
    --UserName qt4s_test \
    --InstanceId tdsql3-789a2481 \
    --Host % \
    --DbName test \
    --ObjectType table
```

Output: 
```
{
    "Response": {
        "Privileges": null,
        "RequestId": "949d8d5e-3622-4a81-9c47-7af93613eeb5"
    }
}
```

