**Example 1: 复制函数**



Input: 

```
tccli scf CopyFunction --cli-unfold-argument  \
    --Namespace default \
    --FunctionName myfunc \
    --TargetNamespace otherns \
    --NewFunctionName newfunc \
    --TargetRegion ap-shanghai \
    --Override FALSE \
    --CopyConfiguration TRUE
```

Output: 
```
{
    "Response": {}
}
```

