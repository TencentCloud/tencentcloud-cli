**Example 1: ExecutePodCommand**

在pod中执行命令

Input: 

```
tccli camp ExecutePodCommand --cli-unfold-argument  \
    --ProjectID abc \
    --ApplicationID abc \
    --EnvironmentName abc \
    --InstanceID abc \
    --UID abc \
    --ContainerName abc \
    --Command abc \
    --Args abc
```

Output: 
```
{
    "Response": {
        "Stdout": "abc",
        "Stderr": "abc",
        "RequestId": "abc"
    }
}
```

