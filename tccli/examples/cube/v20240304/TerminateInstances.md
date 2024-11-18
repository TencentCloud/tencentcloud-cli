**Example 1: 销毁指定ID实例**

用于销毁指定ID的一个或多个实例

Input: 

```
tccli cube TerminateInstances --cli-unfold-argument  \
    --InstanceIds ins-3jaw1j8m
```

Output: 
```
{
    "Response": {
        "RequestId": "9a2f76a2-3b5b-4760-a90b-eff0c611b360"
    }
}
```

**Example 2: 删除实例**

强制删除实例

Input: 

```
tccli cube TerminateInstances --cli-unfold-argument  \
    --InstanceIds eks-1234 \
    --ForceDestroy True
```

Output: 
```
{
    "Response": {
        "RequestId": "7b9c2388-fb6d-4fcb-971c-5f9f6a8b7dfc"
    }
}
```

