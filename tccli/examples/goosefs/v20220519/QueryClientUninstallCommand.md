**Example 1: 查询卸载命令**

查询卸载命令

Input: 

```
tccli goosefs QueryClientUninstallCommand --cli-unfold-argument  \
    --ClusterId x-c60-a112q1lj-client-cluster-default \
    --FileSystemId x-c60-a112q1lj
```

Output: 
```
{
    "Response": {
        "Command": "cd /root/goosefsx_client_agent/linux_client_agent; sh ./uninstall-goosefsx-client.sh\n",
        "RequestId": "ebc942f5-9090-4888-a4c2-5fc87049c6d9"
    }
}
```

