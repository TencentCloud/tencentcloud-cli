**Example 1: 销毁弹性单副本SSD硬盘**

销毁一个或多个弹性单副本SSD硬盘。

Input: 

```
tccli cbs TerminateRemoteDisks --cli-unfold-argument  \
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

