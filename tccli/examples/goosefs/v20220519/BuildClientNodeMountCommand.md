**Example 1: 获取文件系统的客户端挂载命令**

获取某个文件系统的客户端挂载命令

Input: 

```
tccli goosefs BuildClientNodeMountCommand --cli-unfold-argument  \
    --FileSystemId x-c60-053lg6hi \
    --CustomMountDir /test1 \
    --ClusterId x-c60-053lg6hi-client-cluster-default
```

Output: 
```
{
    "Response": {
        "Command": "wget https://gfsx-cfg-bj-***-**********.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh; chmod +x install-goosefsx-client.sh; ./install-goosefsx-client.sh 10.3.30.109:55533,10.3.30.161:55533,10.3.30.181:55533 /test1",
        "RequestId": "92084d7c-416b-4aca-b10e-821df90aeec4"
    }
}
```

