**Example 1: 查询挂载命令**



Input: 

```
tccli goosefs QueryClientNodeMountCommand --cli-unfold-argument  \
    --ClusterId x-c60-a112q1lj-client-cluster-default \
    --ClusterMountInfo.0.StorageFileSystemId x-c60-a112q1lj \
    --ClusterMountInfo.0.MountPoint /mountDir \
    --FileSystemId x-c60-a112q1lj
```

Output: 
```
{
    "Response": {
        "Command": "wget https://***********-***-**********.cos.ap-shanghai.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh; chmod +x install-goosefsx-client.sh; ./install-goosefsx-client.sh ***.***.*.**:55533,***.***.*.**:55533,***.***.*.**:55533 x-c60-a112q1lj:/mountDir",
        "RequestId": "5506922d-4abd-4ca1-ba9e-6f14566b3bd0"
    }
}
```

