**Example 1: 挂载弹性单副本SSD硬盘**

将弹性单副本SSD硬盘挂载到指定的云服务器实例。

Input: 

```
tccli cbs AttachRemoteDisks --cli-unfold-argument  \
    --InstanceId ins-xxxxxxxx \
    --RemoteDiskIds rdisk-b1f7xvod
```

Output: 
```
{
    "Response": {
        "RequestId": "a0ed56a0-4b9a-4690-bd5e-7aa76fd67b4d"
    }
}
```

