**Example 1: 删除集群存储选项信息。**

删除本地挂载点为/data/的存储选项信息。

Input: 

```
tccli thpc DeleteClusterStorageOption --cli-unfold-argument  \
    --ClusterId hpc-5lyv94lq \
    --LocalPath /data/
```

Output: 
```
{
    "Response": {
        "RequestId": "2aeaea7e-9fc4-4c17-8a9b-50343b711003"
    }
}
```

