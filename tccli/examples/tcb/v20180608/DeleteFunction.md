**Example 1: SCF DeleteFunction**



Input: 

```
tccli tcb DeleteFunction --cli-unfold-argument  \
    --EnvId jackvyli-d1g5v7p5e7191af47 \
    --FunctionName scfnodejshelloworldasdf
```

Output: 
```
{
    "Response": {
        "FunctionId": "",
        "RequestId": "f49351aa-0d13-46f9-af46-0f8aebf62e60"
    }
}
```

**Example 2: 删除函数**



Input: 

```
tccli tcb DeleteFunction --cli-unfold-argument  \
    --EnvId cbftest-goreliu-d5f0c7kud1ee02a6 \
    --FunctionName hello
```

Output: 
```
{
    "Response": {
        "FunctionId": "fn-b5366dccb51c67d3",
        "RequestId": "e0303e53-760a-455a-8af8-86bf30c9e821"
    }
}
```

