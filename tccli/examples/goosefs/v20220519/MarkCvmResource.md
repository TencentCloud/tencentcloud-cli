**Example 1: 更换备份资源所属uin**

更换备份资源所属uin

Input: 

```
tccli goosefs MarkCvmResource --cli-unfold-argument  \
    --InstanceIds ins-90vfhebq ins-gwya5yg0 ins-1zsltx2e \
    --OwnerUin 100026787145
```

Output: 
```
{
    "Response": {
        "RequestId": "6dbd7fbf-e0e2-48b9-b5f8-6d013d861f6d"
    }
}
```

