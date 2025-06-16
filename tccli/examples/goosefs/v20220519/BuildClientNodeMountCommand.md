**Example 1: 获取文件系统的客户端挂载命令**

获取某个文件系统的客户端挂载命令

Input: 

```
tccli goosefs BuildClientNodeMountCommand --cli-unfold-argument  \
    --FileSystemId x-c60-a2b3d4 \
    --CustomMountDir /train_data
```

Output: 
```
{
    "Response": {
        "Command": "wget https://goosefsx-bucket-12510000.cos.ap-beijing.myqcloud.com/client_env_package/agent/install-goosefsx-client.sh；chmod +x install-goosefsx-client.sh; ./install-goosefsx-client.sh; 172.3.1.2:55533,172.3.1.3:55533,172.3.1.4:55533 /train_data",
        "RequestId": "c579ea0b-d04f-4cc0-a6e2-fc6bad036017"
    }
}
```

